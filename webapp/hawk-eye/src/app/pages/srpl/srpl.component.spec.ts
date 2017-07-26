import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SrplComponent } from './srpl.component';

describe('SrplComponent', () => {
  let component: SrplComponent;
  let fixture: ComponentFixture<SrplComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SrplComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SrplComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
