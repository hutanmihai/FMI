import {UserRole} from "../models/user";

export interface IUser {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  roles: UserRole[];
  token: string;
}
