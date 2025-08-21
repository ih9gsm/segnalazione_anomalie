describe('index page', () => {
  it('increments counter on click', () => {
    cy.visit('index.html');
    cy.contains('0');
    cy.get('#btn').click();
    cy.contains('1');
  });
});
