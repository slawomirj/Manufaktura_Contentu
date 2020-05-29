# -*- coding: utf-8 -*-
import time

import pytest
from pages.pop_manufaktura import MainManufacture

@pytest.mark.usefixtures("setup")
class TestManufaktura:
    """ Try to search one product witch one brand from household goods in google"""
    def test_household_plus_mark(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        household_plus_mark = MainManufacture(self.driver)
        household_plus_mark.household_plus_mark("RF56N9740SG", "samsung", "Google")

    """ Try to search few products witch one brand from household goods in google
        3 products by default"""
    def test_few_household_plus_mark(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        household_plus_mark = MainManufacture(self.driver)
        household_plus_mark.test_few_household_plus_mark("RF56N9740SG", "WW80R421HFW", "vc07m25e0wr", "Samsung")


    """a large number of tests turn on the captcha"""
    # def test_agd_plus_mark_full(self):
    #     self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
    #     agd_plus_mark = MainManufacture(self.driver)
    #     agd_plus_mark.agd_plus_mark_full("Google")

    """ Try to open a new brand search window"""
    def test_new_mark_open(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        new_mark_open_close = MainManufacture(self.driver)
        new_mark_open_close.new_mark_open_close()

    """ Try to open a new brand search window and search product"""
    def test_household_no_mark(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        household_no_mark = MainManufacture(self.driver)
        household_no_mark.household_no_mark("RF56N9740SG", "Amsung", "Google")

    """ Try to search one product witch one brand from electronics in google"""
    def test_electronic_plus_mark(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        electronic_plus_mark = MainManufacture(self.driver)
        electronic_plus_mark.electronic_plus_mark("T450BT", "JBL", "Google")

    """ Try to search one smartphone witch one brand  in google"""
    def test_smartphone_plus_mark(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        smartphone_plus_mark = MainManufacture(self.driver)
        smartphone_plus_mark.smartphone_plus_mark("iPhone 11", "Apple", "Google")

    """ Try to open 3 portals abount GSM"""
    def test_smartphone_portal(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        smartphone_portal = MainManufacture(self.driver)
        smartphone_portal.smartphones_portals()

    """ Try to search one toy witch one brand in google"""
    def test_toys_plus_mark(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        smart_plus_mark = MainManufacture(self.driver)
        smart_plus_mark.toys_plus_mark("Vickers Wellington", "Cobi", "Google")

    """ Try searching for a PDF file for one product"""
    def test_PDF(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        pdf_search = MainManufacture(self.driver)
        pdf_search.search_pdf("RF56N9740SG", "Google")

    """ Try to search EAN and UPC code in GS1"""
    def test_EAN_UPC(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        ean_upc = MainManufacture(self.driver)
        ean_upc.ean_upc("8801643245092", "193808624407", "Katalog - Produkty w sieci")

    """ Try to search fail EAN and check the message"""
    def test_ean_upc_fail(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        eanupc = MainManufacture(self.driver)
        fail_value = ("18801643245092", "19380862440", "abc", "ABC", "!", "@", "AbC", "1abc", "abc1", "#", " " )
        eanupc.ean_upc_fail(fail_value)

    """Try to open Wetransfer"""
    def test_wetransfer(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        footer_test_1 = MainManufacture(self.driver)
        footer_test_1.check_wetransfer("WeTransfer")

    """Try to open Google Translator"""
    def test_google_translate(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        footer_test_2 = MainManufacture(self.driver)
        footer_test_2.check_google_translate("Tłumacz Google")

    """Try to generate a 10-character password"""
    def test_password_generator(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        footer_test_3 = MainManufacture(self.driver)
        footer_test_3.password_generator()

    """Try to go to page Labels"""
    def test_page_labels(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        page_labels = MainManufacture(self.driver)
        page_labels.page_labels("Etykiety energetyczne", "Etykiety energetyczne")

    """ All test with ..._card, try to enter and open page to create UE energy cards"""
    def test_energy_label_fridge_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        fridge_card = MainManufacture(self.driver)
        fridge_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        fridge_card.energy_label_fridge_card("Lodówki","NR 1060/2010")

    def test_energy_label_hood_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        hood_card = MainManufacture(self.driver)
        hood_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        hood_card.energy_label_hood_card("Okapy", "NR 65/2014")

    def test_energy_label_vacuum_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        vacuum_card = MainManufacture(self.driver)
        vacuum_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        vacuum_card.energy_label_vacuum_card("Odkurzacze", "NR 665/2013")

    def test_energy_label_electric_oven_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        electric_oven_card = MainManufacture(self.driver)
        electric_oven_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        electric_oven_card.energy_label_electric_oven_card("Piekarniki", "NR 65/2014")

    def test_energy_label_gas_oven_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        gas_oven_card = MainManufacture(self.driver)
        gas_oven_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        gas_oven_card.energy_label_gas_oven_card("Piekarniki", "NR 65/2014")

    def test_energy_label_washing_machine_card(self): #zła dyrektywa?
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        washing_machine_card = MainManufacture(self.driver)
        washing_machine_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        washing_machine_card.energy_label_washing_machine_card("Pralki", "NR 1061/2010")

    def test_energy_label_wine_storage_appliances_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        wine_storage_appliances_card = MainManufacture(self.driver)
        wine_storage_appliances_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        wine_storage_appliances_card.energy_label_wine_storage_appliances_card("Lodówki", "NR 643/2009")

    def test_energy_label_air_vented_tumble_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        air_vented_tumble_card = MainManufacture(self.driver)
        air_vented_tumble_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        air_vented_tumble_card.energy_label_air_vented_tumble_card("Suszarki", "NR 392/2012")

    def test_energy_label_pe_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        pe_card = MainManufacture(self.driver)
        pe_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        pe_card.energy_label_pe_card("Płyta elektryczna", "NR 66/2014")

    def test_energy_label_pg_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        pg_card = MainManufacture(self.driver)
        pg_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        pg_card.energy_label_pg_card("Płyta gazowa", "NR 66/2014")

    def test_energy_label_pk_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        pk_card = MainManufacture(self.driver)
        pk_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        pk_card.energy_label_pk_card("Płyta kombinowana", "NR 66/2014")

    def test_energy_label_dishwasher_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        dishwasher_card = MainManufacture(self.driver)
        dishwasher_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        dishwasher_card.energy_label_dishwasher_card("Zmywarki", "NR 1059/2010")

    def test_energy_label_television_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        television_card = MainManufacture(self.driver)
        television_card.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        television_card.energy_label_television_card("TV", "NR 1062/2010")
#----
    """ All test with test_energy_label ...(without card), try to open Energy Label Generator for selected devices """
    def test_energy_label_fridge(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        fridge_label = MainManufacture(self.driver)
        fridge_label.page_labels("Etykiety energetyczne", "Etykiety energetyczne")
        fridge_label.energy_label_fridge("Household refrigerating appliances classified in energy efficiency classes A+++ to C")

    def test_energy_label_hood(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        hood_label = MainManufacture(self.driver)
        hood_label.page_labels("etykieta", "etykiety")
        hood_label.energy_label_hood("Range hood energy label – A++ scale")

    def test_energy_label_electric_oven(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        electric_oven_label = MainManufacture(self.driver)
        electric_oven_label.page_labels("etykieta", "etykiety")
        electric_oven_label.energy_label_electric_oven("Domestic electric ovens energy label")

    def test_energy_label_gas_oven(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        gas_oven_label = MainManufacture(self.driver)
        gas_oven_label.page_labels("etykieta", "etykiety")
        gas_oven_label.energy_label_gas_oven("Domestic gas ovens energy label")

    def test_energy_label_washing_machine(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        washing_machine_label = MainManufacture(self.driver)
        washing_machine_label.page_labels("etykieta", "etykiety")
        washing_machine_label.energy_label_washing_machine("Washing machines energy label")

    def test_energy_label_wine_storage_appliances(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        wine_storage_appliances_label = MainManufacture(self.driver)
        wine_storage_appliances_label.page_labels("etykieta", "etykiety")
        wine_storage_appliances_label.energy_label_wine_storage_appliances("Wine storage appliances classified in energy efficiency classes A+++ To G")

    def test_energy_label_air_vented_tumble(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        air_vented_tumble_label = MainManufacture(self.driver)
        air_vented_tumble_label.page_labels("etykieta", "etykiety")
        air_vented_tumble_label.energy_label_air_vented_tumble("Air vented tumble driers energy label")

    def test_energy_label_dishwasher(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        dishwasher_label = MainManufacture(self.driver)
        dishwasher_label.page_labels("etykieta", "etykiety")
        dishwasher_label.energy_label_dishwasher("Dishwashers energy label")

    def test_energy_label_television(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        television_label = MainManufacture(self.driver)
        television_label.page_labels("etykieta", "etykiety")
        television_label.energy_label_television("Label for Televisions Classes A++ to E")

    def test_energy_label_lamps(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        lamp_label = MainManufacture(self.driver)
        lamp_label.page_labels("etykieta", "etykiety")
        lamp_label.energy_label_lamps("Lamps classified in energy efficiency classes A++ to E")

    def test_energy_tires(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        tires_label = MainManufacture(self.driver)
        tires_label.page_labels("etykieta", "etykiety")
        tires_label.energy_label_tires("Tyres energy label")

    def test_energy_space_heaters(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        heaters_label = MainManufacture(self.driver)
        heaters_label.page_labels("etykieta", "etykiety")
        heaters_label.energy_label_heaters("Space heaters")

    """ Try to open page with copywrite pages"""
    def test_page_CW(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        page_cw = MainManufacture(self.driver)
        page_cw.page_cw("CW", "CW")
    #todo check all pages in CW

    """Try to go to page Meta"""
    def test_page_meta(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        page_meta = MainManufacture(self.driver)
        page_meta.page_meta("meta", "meta")

    """Try to go to page Meta and generate meta tags: device mark product"""
    def test_page_meta_with_data_without_pn(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        page_meta = MainManufacture(self.driver)
        page_meta.page_meta("meta", "meta")
        page_meta.page_meta_with_data_without_pn("Lodówka Electrolux ENN12800AW")

    """Try to go to page Meta and generate meta tags: device mark product and part number"""
    def test_page_meta_with_data_with_pn(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        page_meta = MainManufacture(self.driver)
        page_meta.page_meta("meta", "meta")
        page_meta.page_meta_with_data_with_pn("Lodówka Electrolux ENN 12800 AW 925503036")

    """Try to go to page Opener"""
    def test_page_opener(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        page_opener = MainManufacture(self.driver)
        page_opener.page_opener("Searching for many products", "Searching for many products")

    """Try to go to page Opener and search few produts with different marks"""
    def test_opener_with_data(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        opener_with_data = MainManufacture(self.driver)
        opener_with_data.page_opener("Searching for many products", "Searching for many products")
        opener_with_data.opener_with_data("LG, 50UM7450PLA","Samsung, fold","JBL, SB150")

    """checks households brands names from the table with their value """
    def test_households_names_values(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        households_names_values = MainManufacture(self.driver)
        households_names_values.agd_name_value()

    """checks electronics brands names from the table with their value """
    def test_electronics_name_value(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        electronics_names_values = MainManufacture(self.driver)
        electronics_names_values.electronics_names_values()

    """checks smartphones brands names from the table with their value """
    def test_smartphones_namse_values(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        smartphones_namse_values = MainManufacture(self.driver)
        smartphones_namse_values.smartphones_names_values()

     # """checks toys brands names from the table with their value """
    def test_toys_names_values(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura_Contentu/index.html")
        toys_names_values = MainManufacture(self.driver)
        toys_names_values.toys_names_values()