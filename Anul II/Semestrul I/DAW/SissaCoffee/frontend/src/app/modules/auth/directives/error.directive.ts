import {Directive, ElementRef} from '@angular/core';

@Directive({
  selector: '[appError]'
})
export class ErrorDirective {
  constructor(private el: ElementRef) {
    el.nativeElement.style.color = 'red';
  }
}
