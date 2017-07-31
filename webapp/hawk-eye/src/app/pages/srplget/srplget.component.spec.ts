import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SrplgetComponent } from './srplget.component';

describe('SrplgetComponent', () => {
  let component: SrplgetComponent;
  let fixture: ComponentFixture<SrplgetComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SrplgetComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SrplgetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
