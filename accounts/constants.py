from django.utils.translation import ugettext_lazy as _


class ErrorMessages:
    PARAMETER_ERROR = _('Check if all required parameters are filled')
    ACCURACY_ERROR = _('Check image is correct specie the accuracy is too low')
    DUPLICATE_DATE = _('Pet\'s weight for this day has been imputed already')
    INVALID_DISEASE_TYPE = _('You have sent an invalid disease type, check the list again.')
    NOT_PET_OWNER = _('This user is not the owner of the pet!')
    PET_NOT_FOUND = _('A pet with the given ID does not exist.!')
    PETS_PROFILES_NOT_FOUND = _('This user does not have any pet data saved.!')
    VITALS_NOT_FOUND = _('Vitals data does not exist for the pet!')
    INVALID_OTP = _('You have entered an invalid otp, please try again')
    USER_ACCOUNT_NOT_FOUND = _('A user with the given credential does not exist.')
    USER_ALREADY_EXISTS = _('A user with the given credentials already exists')
    INCORRECT_PASSWORD = _('You have entered an incorrect password, please try again!')
    INVALID_EMAIL = _('You have entered an invalid email address, please try again!')
    INTERNAL_SERVER_ERROR = _('An internal error is encountered!')
    WEIGHT_NOT_FOUND = _('Weight datas not found for the given user')


class SuccessMessages:
    PREDICTION_SUCCESSFUL = _("Breed prediction successful")
    PETS_PROFILES_FOUND = _('Pets profile data for user fetch successful!')
    WEIGHT_FOUND = _('Weight datas fetch for user successfully')
    PET_PROFILE_CREATED = _('Pet profile created successfully!')
    UPDATED_MEDICAL_CONDITION = _('Medical condition updated Successfully')
    VITALS_FOUND = _('Vitals data fetch successful!')
    PET_WEARABLE_SYNC_SUCCESSFUL = _('Pet\'s wearable synchronization successful!')
    SUCCESSFUL_WEIGHT_TRACKING = _('Pet\'s weight imputed successfully!')
    COMPLETE_EMAIL_VERIFICATION = _('Email successfully verified!')
    COMPLETE_PASSWORD_RESET = _('Password reset successful!')
    SENT_EMAIL = _('Email sent successfully!')
    SUCCESSFUL_LOGOUT = _('User logged out successfully!')
    SUCCESSFUL_LOGIN = _('User logged in successfully!')
