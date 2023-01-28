from rest_framework import status

from .utils.utils import ResponseManager


class CustomResponseMixin:
    """
    A mixin for the generic serializer validation and request response
    """

    def response(self, response, data=None):
        return ResponseManager.handle_response(
            errors=response.get("error", None) or response.get("server_error", None),
            message=response.get("success", None),
            data=response.get("data", None) or data,
            status=response.get("status", None) or (status.HTTP_400_BAD_REQUEST if response.get("error", None)
                                                  else status.HTTP_200_OK if response.get("success", None)
            else status.HTTP_500_INTERNAL_SERVER_ERROR if response.get("server_error", None)
            else status.HTTP_201_CREATED),
        )

    def validate_serializer(self, serialized_data):
        if not serialized_data.is_valid():
            return ResponseManager.handle_response(
                errors=list(serialized_data.errors.items())[0][0] + " error",
                message="Payload is not valid",
                status=status.HTTP_400_BAD_REQUEST,
            )
        pass
