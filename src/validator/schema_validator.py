class SchemaValidator:
    def validate(self, schema):
        errors = []

        if schema.meta.confidence_score < 0.2:
            errors.append("Confidence score below actionable threshold")

        if not schema.functional_requirements:
            errors.append("No functional requirements extracted")

        return not errors, errors, schema
