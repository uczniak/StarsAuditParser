# StarsAuditParser
Parses Pokerstars audit files (*.html) to sum up Spin&amp;Go results and total rakeback.

Should work locale-independently (not fully tested). Adds results from rows containing SpinGo tag.
Calculates rakeback by comparing start and end StarsCoins balances and adjusting for any SC spent in the meantime.

Requires: lxml
