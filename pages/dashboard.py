from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = "#__next > div.jss10 > div > div > div > ul:nth-child(2) > div:nth-child(1) > div.MuiListItemText-root.jss29.jss30 > span"
    players_xpath = "#__next > div.jss10 > div > div > div > ul:nth-child(2) > div:nth-child(2) > div.MuiListItemText-root.jss29.jss31 > span"
    polski_xpath = "#__next > div.jss10 > div > div > div > ul:nth-child(5) > div:nth-child(1) > div.MuiListItemText-root > span"
    sign_out_xpath = "#__next > div.jss10 > div > div > div > ul:nth-child(5) > div:nth-child(2) > div.MuiListItemText-root > span"
    players_count_xpath = "#__next > div.jss10 > main > div.MuiGrid-root.jss9.MuiGrid-container.MuiGrid-spacing-xs-2 > div:nth-child(1)"
    matches_count_xpath = "#__next > div.jss10 > main > div.MuiGrid-root.jss9.MuiGrid-container.MuiGrid-spacing-xs-2 > div:nth-child(2)"
    reports_count_xpath = "#__next > div.jss10 > main > div.MuiGrid-root.jss9.MuiGrid-container.MuiGrid-spacing-xs-2 > div:nth-child(3)"
    events_count_xpath = "#__next > div.jss10 > main > div.MuiGrid-root.jss9.MuiGrid-container.MuiGrid-spacing-xs-2 > div:nth-child(4)"
    dev_team_contact_button_xpath = "#__next > div.jss10 > main > div:nth-child(3) > div:nth-child(1) > div > div.MuiCardActions-root.MuiCardActions-spacing > a"
    add_contact_button_xpath = "#__next > div.jss10 > main > div:nth-child(3) > div:nth-child(2) > div > div > a > button"

    pass
