import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SrplsearchComponent } from './srplsearch.component';

describe('SrplsearchComponent', () => {
  let component: SrplsearchComponent;
  let fixture: ComponentFixture<SrplsearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SrplsearchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SrplsearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
