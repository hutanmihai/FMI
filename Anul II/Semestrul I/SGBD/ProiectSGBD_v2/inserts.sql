-- Regions
INSERT INTO regions (region_name)
VALUES ('NA');
INSERT INTO regions (region_name)
VALUES ('EU');
INSERT INTO regions (region_name)
VALUES ('KR');
INSERT INTO regions (region_name)
VALUES ('AS');
INSERT INTO regions (region_name)
VALUES ('TUR');
COMMIT;

-- Teams
INSERT INTO teams (team_name, region_id)
VALUES ('TSM', 1);
INSERT INTO teams (team_name, region_id)
VALUES ('Fnatic', 2);
INSERT INTO teams (team_name, region_id)
VALUES ('SK Telecom T1', 3);
INSERT INTO teams (team_name, region_id)
VALUES ('EDward Gaming', 4);
INSERT INTO teams (team_name, region_id)
VALUES ('Royal Never Give Up', 4);
COMMIT;

-- Roles
INSERT INTO roles (role_name)
VALUES ('Top');
INSERT INTO roles (role_name)
VALUES ('Jungle');
INSERT INTO roles (role_name)
VALUES ('Mid');
INSERT INTO roles (role_name)
VALUES ('ADC');
INSERT INTO roles (role_name)
VALUES ('Support');
COMMIT;

-- Players
-- Players for TSM (Team SoloMid)
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Søren', 'Bjerg', 'Bjergsen', 3, 1, 1);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Mingyi', 'Shen', 'Spica', 2, 1, 1);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Heo', 'Seung-hoon', 'Huni', 1, 1, 1);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Yiliang', 'Peng', 'Doublelift', 4, 1, 1);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Vincent', 'Wang', 'Biofrost', 5, 1, 1);
COMMIT;

-- Players for Fnatic
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Gabriël', 'Rau', 'Bwipo', 1, 2, 2);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Oskar', 'Boderek', 'Selfmade', 2, 2, 2);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Tim', 'Lipovšek', 'Nemesis', 3, 2, 2);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Martin', 'Larsson', 'Rekkles', 4, 2, 2);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Zdravets', 'Galabov', 'Hylissang', 5, 2, 2);
COMMIT;

-- Players for SK Telecom T1
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Kim', 'Dong-ha', 'Khan', 1, 3, 3);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Moon', 'Woo-chan', 'Cuzz', 2, 3, 3);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Lee', 'Sang-hyeok', 'Faker', 3, 3, 3);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Park', 'Jong-ik', 'Teddy', 4, 3, 3);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Lee', 'Jae-wan', 'Effort', 5, 3, 3);
COMMIT;

-- Players for EDward Gaming
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Li', 'Jian', 'Flandre', 1, 4, 4);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Ming', 'Kai', 'Clearlove', 2, 4, 4);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Lee', 'Yeon-jae', 'Scout', 3, 4, 4);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Hu', 'Xian-zhao', 'iBoy', 4, 4, 4);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Tian', 'Xin', 'Meiko', 5, 4, 4);
COMMIT;

-- Players for Royal Never Give Up
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Yan', 'Jun-ze', 'Letme', 1, 4, 5);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Hung', 'Hau-Hsuan', 'Karsa', 2, 4, 5);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Li', 'Yuan-Hao', 'Xiaohu', 3, 4, 5);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Jian', 'Zi-Hao', 'Uzi', 4, 4, 5);
INSERT INTO players (first_name, last_name, summoner_name, role_id, region_id, team_id)
VALUES ('Shi', 'Sen-Ming', 'Ming', 5, 4, 5);
COMMIT;

-- Tournaments
INSERT INTO tournaments (tournament_name, start_date, end_date, location)
VALUES ('Worlds 2022', TO_DATE('2022-09-29', 'YYYY-MM-DD'), TO_DATE('2022-11-06', 'YYYY-MM-DD'), 'Tokyo');
INSERT INTO tournaments (tournament_name, start_date, end_date, location)
VALUES ('Worlds 2021', TO_DATE('2021-09-29', 'YYYY-MM-DD'), TO_DATE('2021-11-06', 'YYYY-MM-DD'), 'Berlin');
INSERT INTO tournaments (tournament_name, start_date, end_date, location)
VALUES ('Worlds 2020', TO_DATE('2020-09-29', 'YYYY-MM-DD'), TO_DATE('2020-11-06', 'YYYY-MM-DD'), 'London');
INSERT INTO tournaments (tournament_name, start_date, end_date, location)
VALUES ('Mid-Season Invitational 2022', TO_DATE('2022-05-09', 'YYYY-MM-DD'), TO_DATE('2022-05-22', 'YYYY-MM-DD'),
        'Reykjavik');
INSERT INTO tournaments (tournament_name, start_date, end_date, location)
VALUES ('Mid-Season Invitational 2021', TO_DATE('2021-05-09', 'YYYY-MM-DD'), TO_DATE('2021-05-22', 'YYYY-MM-DD'),
        'Stockholm');
COMMIT;

-- Matches
INSERT INTO matches (tournament_id, team1_id, team2_id, match_date)
VALUES (1, 1, 2, TO_DATE('2022-10-07', 'YYYY-MM-DD'));
INSERT INTO matches (tournament_id, team1_id, team2_id, match_date)
VALUES (1, 1, 3, TO_DATE('2022-10-08', 'YYYY-MM-DD'));
INSERT INTO matches (tournament_id, team1_id, team2_id, match_date)
VALUES (1, 1, 4, TO_DATE('2022-10-08', 'YYYY-MM-DD'));
INSERT INTO matches (tournament_id, team1_id, team2_id, match_date)
VALUES (1, 1, 5, TO_DATE('2022-10-09', 'YYYY-MM-DD'));
INSERT INTO matches (tournament_id, team1_id, team2_id, match_date)
VALUES (1, 2, 3, TO_DATE('2022-10-10', 'YYYY-MM-DD'));
INSERT INTO matches (tournament_id, team1_id, team2_id, match_date)
VALUES (1, 2, 4, TO_DATE('2022-10-11', 'YYYY-MM-DD'));
INSERT INTO matches (tournament_id, team1_id, team2_id, match_date)
VALUES (1, 2, 5, TO_DATE('2022-10-12', 'YYYY-MM-DD'));
INSERT INTO matches (tournament_id, team1_id, team2_id, match_date)
VALUES (1, 3, 4, TO_DATE('2022-10-13', 'YYYY-MM-DD'));
INSERT INTO matches (tournament_id, team1_id, team2_id, match_date)
VALUES (1, 3, 5, TO_DATE('2022-10-14', 'YYYY-MM-DD'));
INSERT INTO matches (tournament_id, team1_id, team2_id, match_date)
VALUES (1, 4, 5, TO_DATE('2022-10-15', 'YYYY-MM-DD'));
COMMIT;

-- Match Results
INSERT INTO match_results (match_id, winning_team_id)
VALUES (1, 1);
INSERT INTO match_results (match_id, winning_team_id)
VALUES (2, 1);
INSERT INTO match_results (match_id, winning_team_id)
VALUES (3, 1);
INSERT INTO match_results (match_id, winning_team_id)
VALUES (4, 1);
INSERT INTO match_results (match_id, winning_team_id)
VALUES (5, 2);
INSERT INTO match_results (match_id, winning_team_id)
VALUES (6, 2);
INSERT INTO match_results (match_id, winning_team_id)
VALUES (7, 2);
INSERT INTO match_results (match_id, winning_team_id)
VALUES (8, 3);
INSERT INTO match_results (match_id, winning_team_id)
VALUES (9, 3);
INSERT INTO match_results (match_id, winning_team_id)
VALUES (10, 4);
COMMIT;

-- Player stats
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (1, 1, 6, 1, 7, 310);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (2, 1, 4, 0, 10, 110);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (3, 1, 8, 2, 5, 350);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (4, 1, 5, 0, 7, 320);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (5, 1, 0, 1, 14, 45);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (6, 1, 1, 6, 0, 260);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (7, 1, 0, 4, 1, 90);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (8, 1, 2, 8, 1, 280);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (9, 1, 0, 5, 2, 300);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (10, 1, 1, 0, 3, 35);
COMMIT;

INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (1, 2, 4, 2, 6, 315);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (2, 2, 5, 1, 8, 130);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (3, 2, 7, 3, 4, 360);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (4, 2, 3, 1, 9, 290);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (5, 2, 0, 1, 12, 50);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (11, 2, 2, 4, 1, 270);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (12, 2, 1, 5, 2, 80);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (13, 2, 3, 7, 1, 285);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (14, 2, 1, 3, 3, 260);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (15, 2, 1, 0, 4, 45);
COMMIT;

INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (1, 3, 5, 2, 8, 320);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (2, 3, 3, 1, 11, 120);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (3, 3, 7, 3, 6, 340);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (4, 3, 4, 1, 8, 300);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (5, 3, 1, 2, 13, 40);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (16, 3, 2, 5, 1, 280);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (17, 3, 1, 3, 2, 80);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (18, 3, 3, 7, 0, 290);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (19, 3, 1, 4, 3, 270);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (20, 3, 0, 1, 4, 30);
COMMIT;

INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (1, 4, 5, 3, 9, 330);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (2, 4, 6, 1, 7, 110);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (3, 4, 8, 2, 6, 365);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (4, 4, 5, 1, 8, 305);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (5, 4, 0, 2, 15, 55);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (21, 4, 3, 5, 0, 275);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (22, 4, 1, 6, 1, 95);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (23, 4, 2, 8, 2, 295);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (24, 4, 1, 5, 3, 280);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (25, 4, 1, 0, 4, 60);
COMMIT;


INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (6, 5, 4, 2, 6, 310);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (7, 5, 3, 1, 9, 125);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (8, 5, 6, 3, 5, 350);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (9, 5, 3, 1, 7, 295);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (10, 5, 1, 2, 12, 45);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (11, 5, 2, 4, 1, 280);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (12, 5, 1, 3, 2, 90);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (13, 5, 3, 6, 1, 290);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (14, 5, 1, 3, 3, 270);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (15, 5, 0, 1, 4, 30);
COMMIT;

INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (6, 6, 5, 1, 7, 325);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (7, 6, 4, 0, 10, 130);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (8, 6, 7, 2, 5, 375);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (9, 6, 5, 1, 7, 320);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (10, 6, 0, 1, 14, 50);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (16, 6, 1, 5, 0, 290);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (17, 6, 0, 4, 1, 110);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (18, 6, 2, 7, 1, 300);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (19, 6, 1, 5, 2, 310);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (20, 6, 1, 0, 3, 40);
COMMIT;

INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (6, 7, 6, 2, 8, 335);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (7, 7, 5, 1, 11, 140);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (8, 7, 8, 3, 6, 390);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (9, 7, 4, 1, 8, 330);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (10, 7, 1, 2, 13, 55);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (21, 7, 2, 6, 1, 285);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (22, 7, 1, 5, 2, 100);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (23, 7, 3, 8, 1, 305);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (24, 7, 1, 4, 3, 300);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (25, 7, 0, 1, 4, 35);
COMMIT;

INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (11, 8, 5, 1, 7, 315);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (12, 8, 3, 0, 9, 135);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (13, 8, 6, 2, 5, 370);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (14, 8, 4, 1, 7, 295);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (15, 8, 1, 1, 12, 50);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (16, 8, 2, 5, 1, 290);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (17, 8, 1, 3, 2, 90);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (18, 8, 3, 6, 1, 295);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (19, 8, 1, 4, 3, 270);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (20, 8, 0, 1, 4, 30);
COMMIT;

INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (11, 9, 4, 2, 8, 325);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (12, 9, 5, 1, 10, 145);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (13, 9, 7, 3, 6, 380);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (14, 9, 3, 1, 9, 305);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (15, 9, 0, 1, 13, 60);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (21, 9, 2, 4, 1, 300);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (22, 9, 1, 5, 2, 110);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (23, 9, 3, 7, 1, 310);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (24, 9, 1, 3, 3, 290);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (25, 9, 0, 1, 4, 40);
COMMIT;

INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (16, 10, 2, 5, 1, 290);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (17, 10, 1, 3, 2, 90);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (18, 10, 3, 6, 1, 295);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (19, 10, 1, 4, 3, 270);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (20, 10, 0, 1, 4, 30);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (21, 10, 4, 1, 6, 315);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (22, 10, 3, 0, 9, 120);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (23, 10, 6, 2, 5, 350);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (24, 10, 3, 1, 7, 290);
INSERT INTO player_statistics (player_id, match_id, kills, deaths, assists, cs)
VALUES (25, 10, 1, 1, 12, 45);
COMMIT;

-- Champions
INSERT INTO champions (champion_name, role_id)
VALUES ('Gnar', 1);
INSERT INTO champions (champion_name, role_id)
VALUES ('Darius', 1);
INSERT INTO champions (champion_name, role_id)
VALUES ('Fiora', 1);
INSERT INTO champions (champion_name, role_id)
VALUES ('Maokai', 1);
INSERT INTO champions (champion_name, role_id)
VALUES ('Camille', 1);
INSERT INTO champions (champion_name, role_id)
VALUES ('Lee Sin', 2);
INSERT INTO champions (champion_name, role_id)
VALUES ('Elise', 2);
INSERT INTO champions (champion_name, role_id)
VALUES ('Vi', 2);
INSERT INTO champions (champion_name, role_id)
VALUES ('Sejuani', 2);
INSERT INTO champions (champion_name, role_id)
VALUES ('Jarvan IV', 2);
INSERT INTO champions (champion_name, role_id)
VALUES ('Ahri', 3);
INSERT INTO champions (champion_name, role_id)
VALUES ('Orianna', 3);
INSERT INTO champions (champion_name, role_id)
VALUES ('Zed', 3);
INSERT INTO champions (champion_name, role_id)
VALUES ('Syndra', 3);
INSERT INTO champions (champion_name, role_id)
VALUES ('Yasuo', 3);
INSERT INTO champions (champion_name, role_id)
VALUES ('Vayne', 4);
INSERT INTO champions (champion_name, role_id)
VALUES ('Ezreal', 4);
INSERT INTO champions (champion_name, role_id)
VALUES ('Caitlyn', 4);
INSERT INTO champions (champion_name, role_id)
VALUES ('Jhin', 4);
INSERT INTO champions (champion_name, role_id)
VALUES ('KaiSa', 4);
INSERT INTO champions (champion_name, role_id)
VALUES ('Thresh', 5);
INSERT INTO champions (champion_name, role_id)
VALUES ('Braum', 5);
INSERT INTO champions (champion_name, role_id)
VALUES ('Leona', 5);
INSERT INTO champions (champion_name, role_id)
VALUES ('Alistar', 5);
INSERT INTO champions (champion_name, role_id)
VALUES ('Janna', 5);
COMMIT;

-- Champion Picks
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (1, 1, 2);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (1, 2, 7);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (1, 3, 3);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (1, 4, 9);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (1, 5, 15);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (1, 6, 4);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (1, 7, 8);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (1, 8, 5);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (1, 9, 10);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (1, 10, 14);

INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (2, 1, 1);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (2, 2, 6);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (2, 3, 4);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (2, 4, 9);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (2, 5, 14);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (2, 11, 5);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (2, 12, 10);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (2, 13, 7);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (2, 14, 11);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (2, 15, 16);

INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (3, 1, 2);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (3, 2, 7);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (3, 3, 3);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (3, 4, 8);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (3, 5, 14);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (3, 16, 4);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (3, 17, 9);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (3, 18, 6);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (3, 19, 11);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (3, 20, 16);

INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (4, 1, 2);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (4, 2, 6);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (4, 3, 4);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (4, 4, 9);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (4, 5, 14);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (4, 21, 3);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (4, 22, 10);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (4, 23, 8);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (4, 24, 13);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (4, 25, 18);

INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (5, 6, 1);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (5, 7, 2);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (5, 8, 4);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (5, 9, 9);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (5, 10, 14);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (5, 11, 5);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (5, 12, 10);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (5, 13, 8);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (5, 14, 11);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (5, 15, 16);

INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (6, 6, 1);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (6, 7, 2);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (6, 8, 4);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (6, 9, 9);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (6, 10, 14);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (6, 16, 5);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (6, 17, 10);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (6, 18, 8);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (6, 19, 11);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (6, 20, 16);

INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (7, 6, 1);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (7, 7, 2);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (7, 8, 4);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (7, 9, 9);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (7, 10, 14);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (7, 21, 5);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (7, 22, 10);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (7, 23, 8);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (7, 24, 11);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (7, 25, 16);

INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (8, 11, 1);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (8, 12, 2);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (8, 13, 4);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (8, 14, 9);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (8, 15, 14);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (8, 16, 5);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (8, 17, 10);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (8, 18, 8);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (8, 19, 11);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (8, 20, 16);

INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (9, 11, 1);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (9, 12, 2);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (9, 13, 4);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (9, 14, 9);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (9, 15, 14);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (9, 21, 5);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (9, 22, 10);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (9, 23, 8);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (9, 24, 11);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (9, 25, 16);

INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (10, 16, 1);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (10, 17, 2);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (10, 18, 4);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (10, 19, 9);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (10, 20, 14);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (10, 21, 5);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (10, 22, 10);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (10, 23, 8);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (10, 24, 11);
INSERT INTO champion_picks (match_id, player_id, champion_id)
VALUES (10, 25, 16);

COMMIT;

-- Bans
INSERT INTO bans (match_id, champion_id)
VALUES (1, 1);
INSERT INTO bans (match_id, champion_id)
VALUES (1, 6);

INSERT INTO bans (match_id, champion_id)
VALUES (2, 3);
INSERT INTO bans (match_id, champion_id)
VALUES (2, 8);

INSERT INTO bans (match_id, champion_id)
VALUES (3, 5);
INSERT INTO bans (match_id, champion_id)
VALUES (3, 10);

INSERT INTO bans (match_id, champion_id)
VALUES (4, 7);
INSERT INTO bans (match_id, champion_id)
VALUES (4, 12);

INSERT INTO bans (match_id, champion_id)
VALUES (5, 9);
INSERT INTO bans (match_id, champion_id)
VALUES (5, 14);

INSERT INTO bans (match_id, champion_id)
VALUES (6, 11);
INSERT INTO bans (match_id, champion_id)
VALUES (6, 16);

INSERT INTO bans (match_id, champion_id)
VALUES (7, 13);
INSERT INTO bans (match_id, champion_id)
VALUES (7, 18);

INSERT INTO bans (match_id, champion_id)
VALUES (8, 15);
INSERT INTO bans (match_id, champion_id)
VALUES (8, 20);

INSERT INTO bans (match_id, champion_id)
VALUES (9, 17);
INSERT INTO bans (match_id, champion_id)
VALUES (9, 22);

INSERT INTO bans (match_id, champion_id)
VALUES (10, 19);
INSERT INTO bans (match_id, champion_id)
VALUES (10, 24);

COMMIT;
