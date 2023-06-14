import {Injectable} from '@angular/core';
import {environment} from "../../../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {BehaviorSubject, Observable, switchMap, tap} from "rxjs";
import {checkRoles, UserRole} from "../../../models/user";
import {IUser} from "../../../interfaces/user";
import {IUserSignup} from "../../../interfaces/signup";
import {IUserLogin} from "../../../interfaces/login";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private httpClient: HttpClient) {
    const userJson = localStorage.getItem('user');
    this.currentUserSubject = new BehaviorSubject<IUser | null>(userJson ? JSON.parse(userJson) : null);
    this.currentUser$ = this.currentUserSubject.asObservable();
  }

  private currentUserSubject: BehaviorSubject<IUser | null>;
  currentUser$: Observable<IUser | null>;

  get currentUser(): IUser | null {
    return this.currentUserSubject.value;
  }

  checkRole(expectedRole: UserRole): boolean {
    return checkRoles(this.currentUser, expectedRole);
  }

  signUp(user: IUserSignup): Observable<any> {
    return this.httpClient.post(`${environment.apiUrl}/auth/register`, user);
  }

  login(user: IUserLogin): Observable<IUser> {
    return this.httpClient.post(`${environment.apiUrl}/auth/login`, user, {responseType: 'text'})
      .pipe(
        switchMap((token: string) => {
          localStorage.setItem('token', token);
          return this.refreshCurrentUser();
        })
      );
  }

  logout(): void {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    this.currentUserSubject.next(null);
  }

  refreshCurrentUser(): Observable<any> {
    return this.me().pipe(tap((me: Partial<IUser>) => {
      const user = {
        token: localStorage.getItem('token')!,
        ...me
      } as IUser;
      localStorage.setItem('user', JSON.stringify(user));
      this.currentUserSubject.next(user);
    }));
  }

  me(): Observable<Partial<IUser>> {
    return this.httpClient.get<IUser>(`${environment.apiUrl}/users/me`);
  }
}
