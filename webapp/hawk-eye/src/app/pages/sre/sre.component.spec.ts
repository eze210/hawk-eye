import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SreComponent } from './sre.component';

describe('SreComponent', () => {
  let component: SreComponent;
  let fixture: ComponentFixture<SreComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SreComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SreComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
