class SchemaValidator:
    def validate(self, schema):
        errors = []
        if schema.meta.confidence_score < 0.2:
            errors.append("REJECT: Confidence too low")
        return not errors, errors, schema
