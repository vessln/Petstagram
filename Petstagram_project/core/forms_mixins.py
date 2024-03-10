
class ReadonlyFormFieldsMixin:
    readonly_fields = ()

    def _make_fields_readonly(self):
        for field_name in self.readonly_fields_names:
            self.fields[field_name].widget.attrs["readonly"] = "readonly"
            self.fields[field_name].widget.attrs["disabled"] = "disabled"

    @property
    def readonly_fields_names(self):
        if self.readonly_fields == "__all__":
            return self.fields.keys()

        return self.readonly_fields
