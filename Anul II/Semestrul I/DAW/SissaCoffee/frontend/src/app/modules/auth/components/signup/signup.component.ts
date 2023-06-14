import {Component, OnInit} from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {equalToValidator} from "../../../../directives/equal-to.directive";
import {AuthService} from "../../services/auth.service";
import {Router} from "@angular/router";
import {IUserSignup} from "../../../../interfaces/signup";

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  formGroup: FormGroup = new FormGroup({
    'firstName': new FormControl('', Validators.required),
    'lastName': new FormControl('', Validators.required),
    'email': new FormControl('', [Validators.required, Validators.email]),
    'password': new FormControl('', Validators.required),
    'passwordConfirmation': new FormControl('', Validators.required)
  });
  emailAlreadyTaken: boolean = false;

  constructor(private authService: AuthService, private router: Router) {
    this.formGroup.get('passwordConfirmation')?.addValidators(equalToValidator(this.formGroup.get('password')!));
  }

  ngOnInit(): void {
  }

  signup(): void {
    this.authService.signUp(this.formGroup.value as IUserSignup)
      .subscribe({
        next: (_) => {
          this.router.navigate(['/login']);
        },
        error: (res: any) => {
          this.emailAlreadyTaken = true;
        }
      });
  }
}
