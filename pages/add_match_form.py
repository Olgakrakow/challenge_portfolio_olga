from pages.base_page import BasePage


class Dashboard(BasePage):
    my_team_xpath = "#__next > div.jss10 > main > div.MuiPaper-root.MuiCard-root.jss163.MuiPaper-elevation1.MuiPaper-rounded > form > div.MuiCardContent-root > div > div:nth-child(1) > div > div > input"
    enemy_team_xpath = "#__next > div.jss10 > main > div.MuiPaper-root.MuiCard-root.jss163.MuiPaper-elevation1.MuiPaper-rounded > form > div.MuiCardContent-root > div > div:nth-child(2) > div > div > input"
    my_team_score_xpath = "#__next > div.jss10 > main > div.MuiPaper-root.MuiCard-root.jss163.MuiPaper-elevation1.MuiPaper-rounded > form > div.MuiCardContent-root > div > div:nth-child(3) > div > div > input"
    enemy_team_score_xpath = "#__next > div.jss10 > main > div.MuiPaper-root.MuiCard-root.jss163.MuiPaper-elevation1.MuiPaper-rounded > form > div.MuiCardContent-root > div > div:nth-child(4) > div > div > input"
    t_shirt_color_xpath = "#__next > div.jss10 > main > div.MuiPaper-root.MuiCard-root.jss163.MuiPaper-elevation1.MuiPaper-rounded > form > div.MuiCardContent-root > div > div:nth-child(7) > div > div > input"
    match_at_home_xpath = "#__next > div.jss10 > main > div.MuiPaper-root.MuiCard-root.jss163.MuiPaper-elevation1.MuiPaper-rounded > form > div.MuiCardContent-root > div > div:nth-child(6) > fieldset > div > label:nth-child(1) > span.MuiTypography-root.MuiFormControlLabel-label.MuiTypography-body1"
    match_out_home_xpath = "#__next > div.jss10 > main > div.MuiPaper-root.MuiCard-root.jss163.MuiPaper-elevation1.MuiPaper-rounded > form > div.MuiCardContent-root > div > div:nth-child(6) > fieldset > div > label:nth-child(2) > span.MuiTypography-root.MuiFormControlLabel-label.MuiTypography-body1"
    league_xpath = "#__next > div.jss10 > main > div.MuiPaper-root.MuiCard-root.jss163.MuiPaper-elevation1.MuiPaper-rounded > form > div.MuiCardContent-root > div > div:nth-child(8) > div > div > input"
    time_played_xpath = "#__next > div.jss10 > main > div.MuiPaper-root.MuiCard-root.jss163.MuiPaper-elevation1.MuiPaper-rounded > form > div.MuiCardContent-root > div > div:nth-child(9) > div > div > input"
    web_match_xpath = "#__next > div.jss10 > main > div.MuiPaper-root.MuiCard-root.jss163.MuiPaper-elevation1.MuiPaper-rounded > form > div.MuiCardContent-root > div > div:nth-child(11) > div > div > input"

    pass
