# -*- coding: utf-8 -*-
import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainManufacture:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.field_id = "//*[@id='section1_field']"
        self.AGD_xpath = "/html/body/div/div[1]/div[2]/div/div/div[1]/div[1]/h4/a"
        self.no_mark_id = "//*[@id='section1_NewMarkUp']"
        self.new_mark_id = "//*[@id='section1_fieldNewMark']"
        self.new_mark_search_id = "//*[@id='section1_NewMarkSearch']"
        self.RTV_xpath = "/html/body/div/div[1]/div[2]/div/div/div[2]/div[1]/h4/a"
        self.Smart_xpath = "/html/body/div/div[1]/div[2]/div/div/div[3]/div[1]/h4/a"
        self.PDF_xpath = "/html/body/div/div[1]/div[1]/div/button[1]"
        self.search_EAN_UPC_id = "//*[@id='section1_P_W_S']"
        self.button_wetransfer_xpath = "/html/body/div/div[1]/div[1]/div/div[2]/a[5]/button"
        self.button_google_translate_xpath = "/html/body/div/div[1]/div[1]/div/div[2]/a[6]/button"
        self.button_password_generator = "/html/body/div/div[1]/div[1]/div/div[2]/a[7]/button"
        self.button_label_xpath = "//*[@id='section1_label']"
        self.card_fridge_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[2]"
        self.card_header_xpath = "/html/body/div/div/table/thead/tr/th"
        self.card_hood_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/a[2]"
        self.card_vacuum_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/a/s"
        self.card_electric_oven_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/a[2]"
        self.card_gas_oven_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/a[2]"
        self.card_washing_machine_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/a[2]"
        self.card_wine_storage_appliances_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/a[2]"
        self.card_air_vented_tumble_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/a[2]"
        self.card_pe_xpath = "/html/body/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/a"
        self.card_pg_xpath = "/html/body/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/a"
        self.card_pk_xpath = "/html/body/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/a"
        self.card_dishwasher_xpath = "/html/body/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/a[2]"
        self.card_televisions_xpath = "/html/body/div/div/div[2]/div[2]/div[4]/div[1]/div[2]/a[2]"
        self.energy_label_fridge_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[1]"
        self.energy_label_hood_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/a[1]"
        self.energy_label_electric_oven_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/a[1]"
        self.energy_label_gas_oven_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/a[1]"
        self.energy_label_washing_machine_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/a[1]"
        self.energy_label_wine_storage_appliances_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/a[1]"
        self.energy_label_air_vented_tumble_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/a[1]"
        self.energy_label_dishwasher_xpath = "/html/body/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/a[1]"
        self.energy_label_television_xpath = "/html/body/div/div/div[2]/div[2]/div[4]/div[1]/div[2]/a[1]"
        self.energy_label_lamps_xpath = "/html/body/div/div/div[2]/div[2]/div[4]/div[2]/div[2]/a"
        self.energy_label_tires_xpath = "/html/body/div/div/div[2]/div[2]/div[4]/div[3]/div[2]/a"
        self.energy_label_heaters_xpath = "/html/body/div/div/div[2]/div[2]/div[4]/div[4]/div[2]/a"
        self.opener_xpath = "/html/body/div/div[1]/div[1]/div/div[2]/a[4]/button"
        self.opener_text_id = "//*[@id='myTextarea']"
        self.opener_button_xpath = "/html/body/div/div/div[2]/div/button"
        self.cw_button_xpath = "/html/body/div/div[1]/div[1]/div/div/a[2]/button/i"
        self.meta_button_xpath = "/html/body/div/div[1]/div[1]/div/div/a[3]/button/i"
        self.meta_type_input_id = "//*[@id='Rodzaj']"
        self.meta_mark_input_id = "//*[@id='Marka']"
        self.meta_name_input_id = "//*[@id='Nazwa']"
        self.meta_pn_input_id = "//*[@id='Kod']"
        self.meta_button_generator_xpath = "/html/body/div/div/div[2]/div[2]/button"
        self.meta_result_id = "//*[@id='meta_2']"
        self.toys_xpath = "/html/body/div/div[1]/div[2]/div/div/div[5]/div[1]/h4/a"
        self.toys_id_td_xpath = "//*[@id='Toys_Brands_list']/div/table/tbody/tr/td"
        self.smart_id_td_xpath = "//*[@id='Smart_Brands_list']/div/table/tbody/tr/td"
        self.rtv_id_td_xpath = "//*[@id='Elec_Brands_list']/div/table/tbody/tr/td"
        self.agd_id_td_xpath = "//*[@id='HA_Brands_list']/div/table/tbody/tr/td"
        self.info_xpath = "//*[@id='info_message']"


    """ Assert search value from tests
        search_value_temp[0] - tittle of new page
        search_value_temp[1] - search value 
        or 
        svt1  - info about UE directive
    """
    def check_assert(self, search_value):
        global list_value
        list_value = []
        catch_current_window = self.driver.current_window_handle
        catch_window = self.driver.window_handles
        for window in catch_window:
            if window != catch_current_window:
                self.driver.switch_to.window(window)
                if search_value == "need_list":
                    page_url = self.driver.current_url
                    list_value.append(page_url)
                    self.logger.info("Search value: {}".format(list_value))
                else:
                    search_value_temp = search_value.split(",")
                    self.logger.info("Page tittle: {}".format(search_value_temp[0]))
                    self.logger.info("Search value: {}".format(search_value_temp[1]))
                    assert search_value_temp[0] in self.driver.title, "Wrong tittle"
                    checking_for_text = self.driver.find_elements_by_xpath("//*[contains(text(),'" + search_value_temp[1] + "')]")
                    assert len(checking_for_text)>0, "test info"
                self.driver.close()
        self.driver.switch_to.window(catch_current_window)

    """Search household plus mark from list in google """
    def household_plus_mark(self, *args):
        self.driver.find_element_by_xpath(self.field_id).send_keys(args[0])
        self.driver.find_element_by_xpath(self.AGD_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        convert_mark_in_value_apm = args[1].title()
        agd_plus_mark_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@value='" + str(convert_mark_in_value_apm) + "']")))
        agd_plus_mark_element.click()
        search_value_apm = args[2] + ","+ args[0] + " inurl:www." + convert_mark_in_value_apm
        MainManufacture.check_assert(self, search_value_apm)
        self.driver.find_element_by_xpath(self.field_id).clear()

    """Search 3  households products plus mark from list in google """

    def test_few_household_plus_mark(self, *args):
        search_pack = args[0] + "," + args[1] + "," + args[2]
        self.driver.find_element_by_xpath(self.field_id).send_keys(search_pack)
        self.driver.find_element_by_xpath(self.AGD_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        few_agd_plus_mark_elements = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@value='" + args[3] + "']")))
        few_agd_plus_mark_elements.click()
        search_value_fhpm = "need_list"
        MainManufacture.check_assert(self, search_value_fhpm)
        """ args have the reverse order to list_value""" #todo reversed
        few_products_counter = 2
        for i in range(3):
            assert args[few_products_counter] in list_value[i], "Wrong product"
            few_products_counter = few_products_counter - 1
        self.driver.find_element_by_xpath(self.field_id).clear()

    """
    Search household plus all households marks in google
    Blocked by capcha
    """
    def household_plus_mark_full(self, *args):
        self.driver.find_element_by_xpath(self.AGD_xpath).click()
        self.driver.implicitly_wait(5)
        le = self.driver.find_elements_by_xpath(self.agd_id_td_xpath) # todo catch radio button
        le_values = [values_le.get_attribute("textContent") for values_le in le]
        for agd_p in le_values:
            if len(agd_p) > 1:
                try:
                    agd_p = agd_p.strip()
                    self.driver.find_element_by_xpath(self.field_id).send_keys(agd_p)
                    self.driver.find_element_by_xpath("//input[@value='" + agd_p + "']").click()
                    search_value_apmf = "" + args[0] + "," + agd_p + " inurl:www." + agd_p + ""
                    MainManufacture.check_assert(self, search_value_apmf)
                    self.driver.find_element_by_xpath(self.field_id).clear()
                except NoSuchElementException:
                    self.logger.info("FAIL IN {}".format(agd_p))

    """ Open and close new mark on page in google"""
    def new_mark_open_close(self):
        self.driver.find_element_by_xpath(self.no_mark_id).click()
        assert self.driver.find_element_by_xpath(self.new_mark_id).is_displayed() == True, "No display"


    """Search household plus new mark in google"""
    def household_no_mark(self, *args):
        self.driver.find_element_by_xpath(self.field_id).send_keys(args[0])
        MainManufacture.new_mark_open_close()
        self.driver.find_element_by_xpath(self.new_mark_id).send_keys(args[1])
        self.driver.find_element_by_xpath(self.new_mark_search_id).click()
        search_value_anm = args[2] + ","+ args[0] + " inurl:www." + args[1]
        MainManufacture.check_assert(self, search_value_anm)
        self.driver.find_element_by_xpath(self.field_id).clear()


    """Search RTV plus mark from list in google"""
    def electronic_plus_mark(self, *args):
        self.driver.find_element_by_xpath(self.field_id).send_keys(args[0])
        self.driver.find_element_by_xpath(self.RTV_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        convert_mark_in_value_rpm = args[1].title()
        rtv_plus_mark_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='" +convert_mark_in_value_rpm + "']")))
        rtv_plus_mark_element.click()
        search_value_rtp = args[2] + ","+ args[0] + " inurl:www." + convert_mark_in_value_rpm
        MainManufacture.check_assert(self, search_value_rtp)
        self.driver.find_element_by_xpath(self.field_id).clear()

    """Search smartphone plus mark from list in google"""
    def smartphone_plus_mark(self, *args):
        self.driver.find_element_by_xpath(self.field_id).send_keys(args[0])
        self.driver.find_element_by_xpath(self.Smart_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        convert_mark_in_value_spm = args[1].title()
        smart_plus_mark_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@value='" + convert_mark_in_value_spm + "']")))
        smart_plus_mark_element.click()
        search_value_spm = args[2] + ","+ args[0] + " inurl:www." + convert_mark_in_value_spm
        MainManufacture.check_assert(self, search_value_spm)
        self.driver.find_element_by_xpath(self.field_id).clear()

    """Search website about smartfons"""
    def smartphones_portals(self):
        self.driver.find_element_by_xpath(self.Smart_xpath).click()
        self.driver.implicitly_wait(5)
        for i in range(3):
            assert_value = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[" + str(
                    i + 6) + "]/td/a").text
            search_value_sm = assert_value + "," + assert_value
            self.driver.find_element_by_xpath(
                "/html/body/div/div[1]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[" + str(
                    i + 6) + "]/td/a").click()
            MainManufacture.check_assert(self, search_value_sm)

    """Search toys plus mark from list in google"""
    def toys_plus_mark(self, *args):
        self.driver.find_element_by_xpath(self.field_id).send_keys(args[0])
        self.driver.find_element_by_xpath(self.toys_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        convert_mark_in_value_tpm = args[1].title()
        toys_plus_mark_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@value='" + convert_mark_in_value_tpm + "']")))
        toys_plus_mark_element.click()
        search_value_stm = args[2] + ","+ args[0] + " inurl:www." + convert_mark_in_value_tpm
        MainManufacture.check_assert(self, search_value_stm)
        self.driver.find_element_by_xpath(self.field_id).clear()

    """Search pdf in google"""
    def search_pdf(self, *args):
        self.driver.find_element_by_xpath(self.field_id).send_keys(args[0])
        self.driver.find_element_by_xpath(self.PDF_xpath).click()
        search_value_sp = "" + args[1] + "," + args[0] + " filetype:pdf"
        MainManufacture.check_assert(self, search_value_sp)
        self.driver.find_element_by_xpath(self.field_id).clear()

    """Search EAN or UPS in gs1"""
    def ean_upc(self, *args):
        for i in range(2):
            self.driver.find_element_by_xpath(self.field_id).send_keys(args[i])
            self.driver.find_element_by_xpath(self.search_EAN_UPC_id).click()
            search_value_eu = args[2] + "," + args[i]
            MainManufacture.check_assert(self, search_value_eu)
            self.driver.find_element_by_xpath(self.field_id).clear()

    """Search wrong EAN or UPS """
    def ean_upc_fail(self, fail_v):
        fail_v_len = len(fail_v)
        for i in range(fail_v_len):
            self.driver.find_element_by_xpath(self.field_id).send_keys(fail_v[i])
            self.driver.find_element_by_xpath(self.search_EAN_UPC_id).click()
            psw = self.driver.find_element_by_xpath(self.info_xpath).get_attribute("textContent")
            assert "To nie jest kod EAN" in psw, "Bad info"
            self.logger.info("Search value {}".format(fail_v[i]))
            self.driver.find_element_by_xpath(self.field_id).clear()

    """Open wetransfer """
    def check_wetransfer(self, wetransfer):
        self.driver.find_element_by_xpath(self.button_wetransfer_xpath).click()
        search_value_w = "" + wetransfer + "," + wetransfer + ""
        MainManufacture.check_assert(self, search_value_w)

    """Open google translator """
    def check_google_translate(self,google_translate):
        self.driver.find_element_by_xpath(self.button_google_translate_xpath).click()
        search_value_gt = "" + google_translate + "," + google_translate + ""
        MainManufacture.check_assert(self, search_value_gt)

    """Open alert with random password"""
    def password_generator(self):
        self.driver.find_element_by_xpath(self.button_password_generator).click()
        password_info = self.driver.find_element_by_xpath(self.info_xpath).get_attribute("textContent")
        assert len(password_info) == 10, "Password to short"
        self.logger.info("Password {}".format(password_info))

    """open page etykiety"""
    def page_labels(self, *args):
        self.driver.find_element_by_xpath(self.button_label_xpath).click()
        search_value_e = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_e)
    """ 
        In etykiety open page with UE card and open label generator in /ec.europa.eu/energy/eepf-labels 
    """
    def energy_label_fridge_card (self, *args):
        self.driver.find_element_by_xpath(self.card_fridge_xpath).click()
        search_value_elfc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elfc)

    def energy_label_hood_card (self, *args):
        self.driver.find_element_by_xpath(self.card_hood_xpath).click()
        search_value_elhc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elhc)

    def energy_label_vacuum_card (self, *args):
        self.driver.find_element_by_xpath(self.card_vacuum_xpath).click()
        search_value_elvc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elvc)

    def energy_label_electric_oven_card(self, *args):
        self.driver.find_element_by_xpath(self.card_electric_oven_xpath).click()
        search_value_eleoc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_eleoc)

    def energy_label_gas_oven_card(self, *args):
        self.driver.find_element_by_xpath(self.card_gas_oven_xpath).click()
        search_value_elgoc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elgoc)

    def energy_label_washing_machine_card(self, *args):
        self.driver.find_element_by_xpath(self.card_washing_machine_xpath).click()
        search_value_elwmc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elwmc)

    def energy_label_wine_storage_appliances_card(self, *args):
        self.driver.find_element_by_xpath(self.card_wine_storage_appliances_xpath).click()
        search_value_elwsac = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elwsac)

    def energy_label_air_vented_tumble_card(self, *args):
        self.driver.find_element_by_xpath(self.card_air_vented_tumble_xpath).click()
        search_value_elavtc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elavtc)

    def energy_label_pe_card(self, *args):
        self.driver.find_element_by_xpath(self.card_pe_xpath).click()
        search_value_elpc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elpc)

    def energy_label_pg_card(self, *args):
        self.driver.find_element_by_xpath(self.card_pg_xpath).click()
        search_value_elpc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elpc)

    def energy_label_pk_card(self, *args):
        self.driver.find_element_by_xpath(self.card_pk_xpath).click()
        search_value_elpc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elpc)

    def energy_label_dishwasher_card(self, *args):
        self.driver.find_element_by_xpath(self.card_dishwasher_xpath).click()
        search_value_eldc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_eldc)

    def energy_label_television_card(self, *args):
        self.driver.find_element_by_xpath(self.card_televisions_xpath).click()
        search_value_eltc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_eltc)

    def energy_label_fridge (self, refrigerating):
        self.driver.find_element_by_xpath(self.energy_label_fridge_xpath).click()
        search_value_elf = "" + refrigerating + "," + refrigerating + ""
        MainManufacture.check_assert(self, search_value_elf)

    def energy_label_hood (self, hood):
        self.driver.find_element_by_xpath(self.energy_label_hood_xpath).click()
        search_value_elh = "" + hood + "," + hood + ""
        MainManufacture.check_assert(self, search_value_elh)

    def energy_label_electric_oven(self, electric_oven):
        self.driver.find_element_by_xpath(self.energy_label_electric_oven_xpath).click()
        search_value_eleo = "" + electric_oven + "," + electric_oven + ""
        MainManufacture.check_assert(self, search_value_eleo)

    def energy_label_gas_oven(self, gas_oven):
        self.driver.find_element_by_xpath(self.energy_label_gas_oven_xpath).click()
        search_value_elgo = "" + gas_oven + "," + gas_oven + ""
        MainManufacture.check_assert(self, search_value_elgo)

    def energy_label_washing_machine(self, washing_machine):
        self.driver.find_element_by_xpath(self.card_washing_machine_xpath).click()
        search_value_elwm = "" + washing_machine + "," + washing_machine + ""
        MainManufacture.check_assert(self, search_value_elwm)

    def energy_label_wine_storage_appliances(self, wine):
        self.driver.find_element_by_xpath(self.energy_label_wine_storage_appliances_xpath).click()
        search_value_elwsa = "" + wine + "," + wine + ""
        MainManufacture.check_assert(self, search_value_elwsa)

    def energy_label_air_vented_tumble(self, air_vented_tumble):
        self.driver.find_element_by_xpath(self.energy_label_air_vented_tumble_xpath).click()
        search_value_elavt = "" + air_vented_tumble + "," + air_vented_tumble + ""
        MainManufacture.check_assert(self, search_value_elavt)

    def energy_label_dishwasher(self, dishwasher):
        self.driver.find_element_by_xpath(self.energy_label_dishwasher_xpath).click()
        search_value_eld = "" + dishwasher + "," + dishwasher + ""
        MainManufacture.check_assert(self, search_value_eld)

    def energy_label_television(self, tv):
        self.driver.find_element_by_xpath(self.energy_label_television_xpath).click()
        search_value_elt = "" + tv + "," + tv + ""
        MainManufacture.check_assert(self, search_value_elt)

    def energy_label_lamps(self, lamp):
        self.driver.find_element_by_xpath(self.energy_label_lamps_xpath).click()
        search_value_ell = "" + lamp + "," + lamp + ""
        MainManufacture.check_assert(self, search_value_ell)

    def energy_label_tires(self, tier):
        self.driver.find_element_by_xpath(self.energy_label_tires_xpath).click()
        search_value_elt = "" + tier + "," + tier + ""
        MainManufacture.check_assert(self, search_value_elt)

    def energy_label_heaters(self, heater):
        self.driver.find_element_by_xpath(self.energy_label_heaters_xpath).click()
        search_value_elh = "" + heater + "," + heater + ""
        MainManufacture.check_assert(self, search_value_elh)

    """ 404 """
    def page_cw(self, *args):
        self.driver.find_element_by_xpath(self.cw_button_xpath).click()
        search_value_pcw = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_pcw)

    def page_meta(self, *args):
        self.driver.find_element_by_xpath(self.meta_button_xpath).click()
        search_value_pm = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_pm)

    """ checks the operation of the meta generator, does not check the correctness of the generated meta tags
        does not check all variants of data and incorrect entries
    """

    def page_meta_with_data_without_pn(self, product):
        product_s = product.split()
        self.driver.find_element_by_xpath(self.meta_type_input_id).send_keys(product_s[0])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath("//*[contains(text(),'" + product_s[0] + "')]")
        self.driver.find_element_by_xpath(self.meta_mark_input_id).send_keys(product_s[1])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath("//*[contains(text(),'" + product_s[0] + "')][contains(text(),'" + product_s[1] + "')]")
        self.driver.find_element_by_xpath(self.meta_name_input_id).send_keys(product_s[2])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath(
            "//*[contains(text(),'" + product_s[0] + "')][contains(text(),'" + product_s[1] + "')][contains(text(),'" + product_s[2] + "')]")

    """ checks the operation of the meta generator, does not check the correctness of the generated meta tags
        does not check all variants of data and incorrect entries
        """
    def page_meta_with_data_with_pn(self, product):
        product_s = product.split()
        self.driver.find_element_by_xpath(self.meta_type_input_id).send_keys(product_s[0])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath("//*[contains(text(),'" + product_s[0] + "')]")
        self.driver.find_element_by_xpath(self.meta_mark_input_id).send_keys(product_s[1])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath("//*[contains(text(),'" + product_s[0] + "')][contains(text(),'" + product_s[1] + "')]")
        product_s_2 = product_s[2]+" "+product_s[3]+ " "+product_s[4]
        self.driver.find_element_by_xpath(self.meta_name_input_id).send_keys(product_s_2)
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath(
            "//*[contains(text(),'" + product_s[0] + "')][contains(text(),'" + product_s[1] + "')][contains(text(),'" + product_s_2 + "')]")
        self.driver.find_element_by_xpath(self.meta_pn_input_id).send_keys(product_s[5])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath(
            "//*[contains(text(),'" + product_s[0] + "')][contains(text(),'" + product_s[
                1] + "')][contains(text(),'" + product_s_2 + "')][contains(text(),'" + product_s[5] + "')]")


    def page_opener(self, *args):
        self.driver.find_element_by_xpath(self.opener_xpath).click()
        search_value_n = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_n)

    def opener_with_data(self, *args):
        # self.driver.find_element_by_xpath(self.niuch_source_id).send_keys(args[0])
        self.driver.find_element_by_xpath(self.opener_text_id).send_keys(args[0]+"\n"+args[1]+"\n" +args[2])
        self.driver.find_element_by_xpath(self.opener_button_xpath).click()
        search_value_owd = "need_list"
        MainManufacture.check_assert(self, search_value_owd)
        """
        list list_value has inverse values than args, opener_counter count to 0
        """
        opener_counter = 2
        for i in range(3):
            part_name = args[opener_counter].split(",")
            assert part_name[0] in list_value[i], "Wrong product"
            # assert part_name[1] in opener_list_value[i], "Wrong mark"
            opener_counter = opener_counter-1

    """In AGD: gets the content of the td element and compares it with its value"""

    """in Name_value comparison in terms of form of writing (case sensitive)"""

    def agd_name_value(self):
        self.driver.find_element_by_xpath(self.AGD_xpath).click()
        le = self.driver.find_elements_by_xpath(self.agd_id_td_xpath) # todo catch radio button
        le_values = [values_le.get_attribute("textContent") for values_le in le]
        for agd_p in le_values:
            if len(agd_p) > 1:
                try:
                    agd_p = agd_p.strip()
                    le_temp = self.driver.find_element_by_xpath("//input[@value='" + agd_p + "']").get_attribute("value")
                    assert agd_p == le_temp, "Test fail: no mark "+agd_p+""
                except NoSuchElementException:
                    self.logger.info("FAIL IN {}".format(agd_p))

    """In RTV: gets the content of the td element and compares it with its value"""
    def electronics_names_values(self):
        self.driver.find_element_by_xpath(self.RTV_xpath).click()
        lr = self.driver.find_elements_by_xpath(self.rtv_id_td_xpath) # todo catch radio button
        lr_values = [values_lr.get_attribute("textContent") for values_lr in lr]
        for rtv_p in lr_values:
            if len(rtv_p) > 1:
                try:
                    rtv_p = rtv_p.strip()
                    le_temp = self.driver.find_element_by_xpath("//input[@value='" + rtv_p + "']").get_attribute("value")
                    assert rtv_p == le_temp, "Test fail: no mark "+rtv_p+""
                except NoSuchElementException:
                    self.logger.info("FAIL IN {}".format(rtv_p))

    """In Smart: gets the content of the td element and compares it with its value"""
    def smartphones_names_values(self):
        self.driver.find_element_by_xpath(self.Smart_xpath).click()
        ls = self.driver.find_elements_by_xpath(self.smart_id_td_xpath)  # todo catch radio button
        ls_values = [values_ls.get_attribute("textContent") for values_ls in ls]
        for smart_p in ls_values:
            if len(smart_p) > 1:
                try:
                    smart_p = smart_p.strip()
                    le_temp = self.driver.find_element_by_xpath("//input[@value='" + smart_p + "']").get_attribute(
                        "value")
                    self.logger.info("{x} === {y}".format(x=smart_p, y =le_temp))
                    assert smart_p == le_temp, "Test fail: no mark " + smart_p + ""
                except NoSuchElementException:
                    self.logger.info("FAIL IN {}".format(smart_p))

    """In toys: gets the content of the td element and compares it with its value"""
    # todo page names different from td content (e.g. .com)
    def toys_names_values(self):
        self.driver.find_element_by_xpath(self.toys_xpath).click()
        lt = self.driver.find_elements_by_xpath(self.toys_id_td_xpath)  # todo catch radio button
        lt_values = [values_lt.get_attribute("textContent") for values_lt in lt]
        for toys_p in lt_values:
            if len(toys_p) > 1:
                try:
                    toys_p = toys_p.strip()
                    lt_temp = self.driver.find_element_by_xpath("//input[@value='" + toys_p + "']").get_attribute(
                    "value")
                    assert toys_p == lt_temp, "Test fail: no mark " + toys_p + ""
                except NoSuchElementException:
                    self.logger.info("FAIL IN {}".format (toys_p))