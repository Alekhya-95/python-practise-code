from guard import *
import guard

# This function will return the user & facility details for current & parent level.
def getCurrentUserDetails(user_Id):
    user_details = {}
    try:
        cloud_logger.info("Getting assignee details.")
        with spnDB.snapshot() as snapshot:
            query = 'SELECT um.user_id AS current_user_id, fr.facility_name AS current_facility_name,fr.facility_id AS current_facility_id,fr.facility_level AS current_facility_level,urm.role_code AS current_role_code,um.phr_role AS current_phr_role,fr1.facility_name AS parent_facility_name,fr1.facility_id AS parent_facility_id, fr1.facility_level AS parent_facility_level,FROM user_master um LEFT JOIN facility_registry fr ON um.facility_id = fr.facility_id LEFT JOIN user_role_master urm ON urm.role_id = um.role LEFT JOIN facility_registry fr1 ON fr.parent_facility = fr1.facility_id WHERE um.user_id = @userId'
            results = snapshot.execute_sql(
                query,
                params= {
                "userId": user_Id
            },
            param_types={
                "userId": param_types.STRING
            })
            for row in results:
                user_details = {
                    "userId": row[0],
                    "currentFacilityName": row[1],
                    "currentFacilityId": row[2],
                    "currentFacilityLevel": row[3], # HSC / PHC / Block
                    "currentRoleCode":row[4],
                    "currentPhrRole":row[5],
                    "parentFacilityName":row[6],
                    "parentFacilityId":row[7],
                    "parentFacilityLevel":row[8], # PHC / Block 
                }

    except Exception as e:
        cloud_logger.error("Error while fetching User Details : %s | %s | %s ", str(e), guard.current_userId, guard.current_appversion)
        return user_details

    finally:
        return user_details

# This function will return the list of user roles to which the task shall get assigned.
def get_assignee_info(userId, user_action, familyId, memberId): 
    
    user_details = getCurrentUserDetails(userId)
    cloud_logger.info("Getting Current user details - %s | FamilyId : %s | MemberId : %s", str(user_details), familyId, memberId)
    if (user_details and user_action != ''):
        data, isValid = get_assignee_from_facility_level(user_details, user_action, familyId, memberId)

    return data, isValid

def get_facility_id_by(familyId, memberId):
    facilityId = ''
    isAvailable = False
    try:
        cloud_logger.info("Getting facility id from memberId %s and familyId %s", familyId, memberId)
        with spnDB.snapshot() as snapshot:
            query = 'SELECT facility_id from family_member_master WHERE family_id=@familyId and member_id=@memberId'
            results = snapshot.execute_sql(
                query,
                params= {
                "familyId": familyId,
                "memberId": memberId
            },
            param_types={
                "familyId": param_types.STRING,
                "memberId": param_types.STRING
            })
            for row in results:
                facilityId = row[0]
                isAvailable = True
                    
    except Exception as e:
        cloud_logger.error("Error while fetching Facility Id : %s | %s | %s ", str(e), guard.current_userId, guard.current_appversion)
        return isAvailable, facilityId

    finally:
        return isAvailable, facilityId


def get_assignee_from_facility_level(user_details, user_action, familyId, memberId):
    approverRoles = []
    reviewStatus = ''
    reviewMsg = ''
    facilityId = ''
    assignee_role_list = config.getAssineeRole()
    fieldLevelVerifiers = assignee_role_list["Community"]
    firstLevelApprovers =  assignee_role_list["HSC"] 
    secondLevelApprovers = assignee_role_list["PHC"] 
    finalApprovers = assignee_role_list["Block"] 

    data = {}
    
    try:
        cloud_logger.info("Getting assignee details.")
                
        if user_details['currentFacilityLevel']=='COMMUNITY' :
            if (user_details['currentRoleCode'] in fieldLevelVerifiers):
                reviewStatus = 'InProgress'
                approverRoles = firstLevelApprovers
                
        elif user_details['currentFacilityLevel']=='HSC':
            isAvailable, currentBeneficiaryFacilityId = get_facility_id_by(familyId, memberId)
            if isAvailable and (currentBeneficiaryFacilityId == user_details['currentFacilityId']):
                if (user_details['currentRoleCode'] not in firstLevelApprovers):
                    if user_details['currentRoleCode'] == 'WHV':
                        reviewStatus = 'InProgress'
                        approverRoles = firstLevelApprovers
                    else:
                        reviewStatus = 'InProgress'
                        approverRoles = fieldLevelVerifiers
                    facilityId = user_details['currentFacilityId']
                else:
                    reviewStatus = 'InProgress'
                    if user_details['parentFacilityLevel'] == 'PHC':
                        approverRoles = secondLevelApprovers
                        facilityId = user_details['parentFacilityId']
                    elif user_details['parentFacilityLevel'] == 'Block':
                        approverRoles = finalApprovers
                        facilityId = user_details['parentFacilityId']
                    else:
                        reviewStatus = 'FAILED'
                        reviewMsg = 'No valid parent facility available.'
                        cloud_logger.error('No valid parent facility available.')
            else:
                if user_action == 'INITIATED':
                    if currentBeneficiaryFacilityId == '' or currentBeneficiaryFacilityId == None:
                        cloud_logger.error('Facility details are not available for Family Id : %s, Member Id : %s', familyId, memberId)
                    else:
                        reviewStatus = 'InProgress'
                        approverRoles = fieldLevelVerifiers
                        facilityId = currentBeneficiaryFacilityId
                else:
                    reviewStatus = 'FAILED'
                    reviewMsg = 'The User is not eligible to APPROVE.'
                    cloud_logger.error('The User is not eligible to APPROVE.')

        elif user_details['currentFacilityLevel']=='PHC':
            if user_action == 'APPROVED':
                if (user_details['currentRoleCode'] not in secondLevelApprovers):
                    reviewStatus = 'FAILED'
                    reviewMsg = 'The user does not have approver access.'
                    cloud_logger.error('The user does not have approver access.')
                else:
                    if user_details['parentFacilityLevel'] == 'Block':
                        reviewStatus = 'IN_PROGRESS'
                        approverRoles = finalApprovers
                        facilityId = user_details['parentFacilityId']
                    else:
                        reviewStatus = 'FAILED'
                        reviewMsg = 'The parent facility is incorrectly mapped.'
                        cloud_logger.error('The parent facility is incorrectly mapped.') 
            else:
                reviewStatus = 'IN_PROGRESS'
                approverRoles = fieldLevelVerifiers
                if (len(familyId)!=0 and len(memberId)!=0 ) :
                    isavailable, facId = get_facility_id_by(familyId, memberId)
                    if isavailable and facId != '':
                        facilityId = facId
                    else:
                        reviewStatus = 'FAILED'
                        reviewMsg = 'No Facility Id available for Beneficiary.'
                        cloud_logger.error("No data available for given family_id %s & member id : %s", familyId, memberId)
                else:
                    cloud_logger.error("Invalid family_id %s & member id : %s", familyId, memberId)
                    reviewStatus = 'FAILED'
                    reviewMsg = 'Invalid family or member Id.'
                        
        elif user_details['currentFacilityLevel']=='Block':
            if user_action == 'INITIATED':
                reviewStatus = 'IN_PROGRESS'
                approverRoles = fieldLevelVerifiers
                isavailable, facId = get_facility_id_by(familyId, memberId)
                if isavailable and facId != '':
                    facilityId = facId
                else:
                    reviewStatus = 'FAILED'
                    reviewMsg = 'No Facility Id available for Beneficiary.'
                    cloud_logger.error("No data available for given family_id %s & member id : %s", familyId, memberId)

            elif user_action == 'APPROVED':
                if (user_details['currentRoleCode'] not in finalApprovers):
                    reviewStatus = 'FAILED'
                    reviewMsg = 'The User is not eligible to APPROVE.'
                    cloud_logger.error('The User is not eligible to APPROVE.') 
                else:
                    reviewStatus = 'COMPLETED'
                    reviewMsg = 'The approval process is complete.'
                    cloud_logger.error('The approval process is complete.') 
            else:
                reviewStatus = 'FAILED'
                reviewMsg = 'Invalid User Action.'
                cloud_logger.error('Invalid User Action.') 

        data['review_status']=reviewStatus
        data['review_msg']=reviewMsg
        data['facility_id']=facilityId
        data['approver_roles']=approverRoles
        
    except Exception as e:
        cloud_logger.error("Error while fetching assignee Details : %s | %s | %s ", str(e), guard.current_userId, guard.current_appversion)
        return data, False

    finally:
        return data, True