import {AbstractControl, ValidationErrors, ValidatorFn} from "@angular/forms";

export function equalToValidator(other: AbstractControl): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const equal = control.value === other.value;
    return equal ? null : { equalTo: { me: control.value, them: other.value } };
  };
}
