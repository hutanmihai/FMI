import {IUser} from "../interfaces/user";

export enum UserRole {
  Admin = 'Admin',
  Customer = 'Customer'
}

export function rolesAtLeast(role: UserRole): UserRole[] {
  switch (role) {
    case UserRole.Customer:
      return [UserRole.Customer, UserRole.Admin];
    case UserRole.Admin:
      return [UserRole.Admin];
    default:
      return [];
  }
}

export function checkRoles(user: IUser | null, expectedRole: UserRole): boolean {
  if (!user) {
    return false;
  }
  const allowedRoles = rolesAtLeast(expectedRole);
  return allowedRoles.some((r: UserRole) => user.roles.includes(r));
}
