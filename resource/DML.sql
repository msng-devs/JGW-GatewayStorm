INSERT INTO METHOD (METHOD_PK, METHOD_NM)
VALUES  (4, 'DELETE'),
        (1, 'GET'),
        (5, 'PATCH'),
        (2, 'POST'),
        (3, 'PUT');

INSERT INTO ROLE (ROLE_PK, ROLE_NM)
VALUES  (4, 'ROLE_ADMIN'),
        (5, 'ROLE_DEV'),
        (1, 'ROLE_GUEST'),
        (0, 'ROLE_NEWGUEST'),
        (3, 'ROLE_UESR1'),
        (2, 'ROLE_USER0');

INSERT INTO ROUTE_OPTION (ROUTE_OPTION_PK, ROUTE_OPTION_NM)
VALUES  (2, 'AUTH'),
        (5, 'AUTH_OPTIONAL'),
        (1, 'NO_AUTH'),
        (3, 'ONLY_TOKEN_AUTH'),
        (4, 'RBAC');

INSERT INTO SERVICE (SERVICE_PK, SERVICE_NM, SERVICE_DOMAIN, SERVICE_INDEX)
VALUES  (1, 'test', 'http://localhost:3000', 'test'),
        (2, 'test2', 'http://localhost:3001', 'test2');

INSERT INTO API_ROUTE (API_ROUTE_PK, API_ROUTE_PATH, METHOD_METHOD_PK, ROLE_ROLE_PK, SERVICE_SERVICE_PK, ROUTE_OPTION_ROUTE_OPTION_PK)
VALUES  (1, '/api/v1/post', 1, 5, 1, 4),
        (2, '/api/v1/post', 2, NULL, 1, 1),
        (3, '/api/v1/member', 4, NULL, 2, 1),
        (4, '/api/v1/member', 3, NULL, 2, 3);






