 Test Plan: ParaBank Web Automation

1. Purpose

The purpose of this project is to build a small but realistic automated test suite for a banking-style web application and to document the testing process around it the way a QA team would. ParaBank is a demo banking site, so it lets me practice testing core financial flows such as logging in, moving money, and paying bills without touching real accounts or real data. The project also serves as a learning exercise and as a portfolio piece showing both manual test design and UI automation.

2. Scope

The following features of ParaBank are in scope and will be covered by both manual test cases and automated tests.

Login. Valid login, invalid username or password, empty fields, and logout behavior. These tests check that only valid users get access and that error messages are shown correctly.

Fund Transfer. Transfer between a user's own accounts, boundary values for the amount (zero, negative, very large, non-numeric), insufficient balance, and whether balances update correctly after a transfer.

Bill Pay. Paying a payee with valid details, missing or invalid fields (account number mismatch, empty payee name, invalid amount), and confirmation of the payment on the result page and in account activity.

3. Out of Scope

The following items will not be tested in this project. Real banking or fintech applications are excluded because testing them without authorization is not appropriate, and ParaBank is used as a safe stand-in. Performance, load, and stress testing are excluded because the demo site is a shared public resource and is not built to handle such traffic. Security and penetration testing, mobile app testing, API-level automation, and cross-browser testing beyond Chrome are also excluded for now and may be added in a later version.

4. Test Approach

Test cases are first designed manually from the requirements of each feature, using techniques such as equivalence partitioning and boundary value analysis. The stable, high-value cases are then automated using the Page Object Model so that locators and page actions are kept separate from test logic. Tests are grouped by feature and by type (smoke, positive, negative) using Pytest markers so that a quick smoke run and a full regression run are both possible. Any genuine application defect found during execution is logged as a GitHub Issue using the bug report template, with the failing test name and a screenshot attached.

5. Tools and Technologies

Purpose Tool 

Programming language: Python 3.11 
UI automation Selenium WebDriver 
Test framework | Pytest |
| Reporting | pytest-html (HTML report) |
| Version control | Git and GitHub |
| Bug tracking | GitHub Issues |

6. Test Environment

 Item Detail

| Application under test | ParaBank demo site (parabank.parasoft.com) |
| Browser | Google Chrome (latest stable) |
| Operating system | Windows |
| Test data | Users registered during test runs, with randomly generated usernames to avoid clashes |

7. Entry and Exit Criteria

Testing starts when the ParaBank site is reachable, the Python environment and dependencies are installed, and the test cases for the feature are written. Testing for a feature is considered complete when all planned test cases have been executed, all automated smoke tests pass on a clean run, and every confirmed defect has been logged with clear steps to reproduce.

8. Deliverables

The project will produce this test plan, a set of manual test cases, the automated Pytest suite, an HTML execution report, and a set of bug reports on GitHub Issues.

9. Risks and Mitigation

| Risk | Impact | Mitigation |

| The demo site goes down or is slow | Tests fail for reasons unrelated to the code | Re-run before reporting a failure, and use explicit waits instead of fixed sleeps |
| The demo database is reset periodically | Previously created users and accounts disappear | Create fresh test data at the start of each run instead of relying on old data |
| Locators change or are unstable | Automated tests break | Keep locators inside page objects so they can be fixed in one place |
| A test fails because of a script problem, not an app bug | False bug reports | Confirm every suspected bug manually before logging it |
| Shared public site behaves differently under load | Flaky results | Run tests sequentially and keep the suite small and focused |

10. Assumptions

ParaBank remains publicly available during the project, its core features (login, transfer, bill pay) behave as documented, and no real or personal data is used at any point.
