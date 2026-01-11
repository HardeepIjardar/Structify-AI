from src.models import RejectionResponse


class RejectionHandler:
    def check(self, errors):
        if errors:
            return RejectionResponse(
                rejection_reason="Input rejected: " + "; ".join(errors)
            )
        return None
