import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as patches
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
from mahjong.meld import Meld
from mahjong.constants import EAST, SOUTH, WEST, NORTH

def print_hand_result(hand_result):
     print(hand_result.han, hand_result.fu)
     print(hand_result.cost['main'], result.cost['additional'])
     print(hand_result.yaku)
     for fu_item in hand_result.fu_details:
          print(fu_item)
     print('')

calculator = HandCalculator()

class ClassCheckMahjongtiles:
    def __init__(self):
        self.Img = '5.png'
        self.ManzuInHandtile = []
        self.SozuInHandtile = []
        self.PinzuInHandtile = []
        self.ZihaiInHandtile = []
        
        self.ManzuTemplates = [
            ['1','Templates/Manzu/p_ms1_1.png'],
            ['2','Templates/Manzu/p_ms2_1.png'],
            ['3','Templates/Manzu/p_ms3_1.png'],
            ['4','Templates/Manzu/p_ms4_1.png'],
            ['5','Templates/Manzu/p_ms5_1.png'],
            ['6','Templates/Manzu/p_ms6_1.png'],
            ['7','Templates/Manzu/p_ms7_1.png'],
            ['8','Templates/Manzu/p_ms8_1.png'],
            ['9','Templates/Manzu/p_ms9_1.png']
            ]
        self.SozuTemplates = [
            ['1','Templates/Pinzu/p_ps1_1.png'],
            ['2','Templates/Pinzu/p_ps2_1.png'],
            ['3','Templates/Pinzu/p_ps3_1.png'],
            ['4','Templates/Pinzu/p_ps4_1.png'],
            ['5','Templates/Pinzu/p_ps5_1.png'],
            ['6','Templates/Pinzu/p_ps6_1.png'],
            ['7','Templates/Pinzu/p_ps7_1.png'],
            ['8','Templates/Pinzu/p_ps8_1.png'],
            ['9','Templates/Pinzu/p_ps9_1.png']
            ]
        self.PinzuTemplates = [
            ['1','Templates/Sozu/p_ss1_1.png'],
            ['2','Templates/Sozu/p_ss2_1.png'],
            ['3','Templates/Sozu/p_ss3_1.png'],
            ['4','Templates/Sozu/p_ss4_1.png'],
            ['5','Templates/Sozu/p_ss5_1.png'],
            ['6','Templates/Sozu/p_ss6_1.png'],
            ['7','Templates/Sozu/p_ss7_1.png'],
            ['8','Templates/Sozu/p_ss8_1.png'],
            ['9','Templates/Sozu/p_ss9_1.png']
            ]
        self.ZihaiTemplates = [
            ['1','Templates/Zihai/p_ji_c_1.png'],
            ['2','Templates/Zihai/p_ji_e_1.png'],
            ['3','Templates/Zihai/p_ji_h_1.png'],
            ['4','Templates/Zihai/p_ji_n_1.png'],
            ['5','Templates/Zihai/p_ji_s_1.png'],
            ['6','Templates/Zihai/p_ji_w_1.png'],
            ['7','Templates/Zihai/p_no_1.png']
            ]
        
        pass
    def __enter__(self):
        pass
    
    def CheckManzu(self):
        count = 0
        for Template in self.ManzuTemplates:
            img_rgb = cv2.imread(self.Img)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread(Template[1],0)
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where( res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                self.ManzuInHandtile.append(Template[0])

    def CheckSozu(self):
        for Template in self.SozuTemplates:
            img_rgb = cv2.imread(self.Img)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread(Template[1],0)
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where( res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                self.SozuInHandtile.append(Template[0])

    def CheckPinzu(self):
        for Template in self.PinzuTemplates:
            img_rgb = cv2.imread(self.Img)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread(Template[1],0)
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where( res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                self.PinzuInHandtile.append(Template[0])

    def CheckZihai(self):
        for Template in self.ZihaiTemplates:
            img_rgb = cv2.imread(self.Img)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread(Template[1],0)
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where( res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                self.ZihaiInHandtile.append(Template[0])

    
    def OutputHandConbination(self):
        Manzu = ''
        Sozu = ''
        Pinzu = ''
        Zihai = ''        
        
        if not len(self.ManzuInHandtile) == 0:
            Manzu = ''.join(self.ManzuInHandtile)
            
        if not len(self.SozuInHandtile) == 0:
            Sozu = ''.join(self.SozuInHandtile)
        
        if not len(self.PinzuInHandtile) == 0:
            Pinzu = ''.join(self.PinzuInHandtile)
        
        if not len(self.ZihaiInHandtile) == 0:
            Zihai = ''.join(self.ZihaiInHandtile)
        
        return [str(Manzu), str(Sozu), str(Pinzu), str(Zihai)]

    
    def __exit__(self):
        pass
    
check = ClassCheckMahjongtiles()
check.CheckManzu()
check.CheckPinzu()
check.CheckSozu()
check.CheckZihai()

Manzu, Sozu, Pinzu, Zihai = check.OutputHandConbination()

tiles = TilesConverter.string_to_136_array(man=Manzu, pin=Pinzu, sou=Sozu, honors=Zihai, has_aka_dora=False)

win_tile = TilesConverter.string_to_136_array(man='2')[0]

melds = None

dora_indicators = None

config = HandConfig(is_tsumo=False, is_ippatsu=False, is_rinshan=False, is_chankan=False, is_haitei=False, is_houtei=False, is_daburu_riichi=False, is_nagashi_mangan=False, is_tenhou=False, is_renhou=False, is_chiihou=False, options=OptionalRules(has_open_tanyao=False, has_aka_dora=False, kazoe_limit=HandConfig.KAZOE_LIMITED))

result = calculator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)
print_hand_result(result)