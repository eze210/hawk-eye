import { HawkEyePage } from './app.po';

describe('hawk-eye App', () => {
  let page: HawkEyePage;

  beforeEach(() => {
    page = new HawkEyePage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
