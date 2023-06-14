import {Pipe, PipeTransform} from '@angular/core';
import {IUser} from "../interfaces/user";

@Pipe({
  name: 'fullName'
})
export class FullNamePipe implements PipeTransform {
  transform(user: IUser | null, ...args: any[]): string {
    if (!user) {
      return 'N/A';
    }
    return `${user.firstName} ${user.lastName}`;
  }
}
