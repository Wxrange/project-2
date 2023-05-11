



from PyQt5.QtWidgets import *
from rocket_league_training_finder import *
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    Controller Class is the details of the proccessing of user input
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_SubmitData.clicked.connect(lambda: self.process_input())
        print('1')

    def process_input(self) -> None:
        """
        The method proccess_input proccesses the input and vailidates the input (maybe expand little more)
        :return None:
        """
        position_count: int = self.lineEdit_Position.text()
        boost_management_count: int = self.lineEdit_BoostManagement.text()
        aerial_shots_count: int = self.lineEdit_AerialShot.text()
        ground_shots_count: int = self.lineEdit_GroundShot.text()
        mechanic_count: int = self.lineEdit_Mechanic.text()
        mechanic_type: str = self.lineEdit_MechanicType.text()
        game_title: str = self.lineEdit_GameTitile.text()


        # check if right value position,boost_management, aerial_shots, ground_shots,mechanic are int, mechanic_type as a string

        error: str = ""
        try:
            position_count = int(position_count)
            boost_management_count = int(boost_management_count)
            ground_shots_count = int(ground_shots_count)
            aerial_shots_count = int(aerial_shots_count)
            mechanic_count = int(mechanic_count)
        except ValueError:
            self.textBrowser_TrainingFocus.setText("Value Error: Enter a integer number (0,1,2,3,etc)")
            print("Value error")
            error = "Error"


        # sort order of counts
        list_mistake_count = [position_count, boost_management_count, aerial_shots_count, ground_shots_count, mechanic_count]
        if error == "":
            for i in range(len(list_mistake_count)):
                print('3')
                i += 1
                m = 0
                while m < len(list_mistake_count):
                    print(f"{m} 4")
                    if m + 1 < len(list_mistake_count):
                        print('5')
                        item_1 = list_mistake_count[m]
                        item_2 = list_mistake_count[m + 1]
                        print("5v2")
                        if item_1 > item_2:
                            print(f"{m} 6")
                            list_mistake_count[m] = item_2
                            list_mistake_count[m + 1] = item_1
                            m += 1
                        else:
                            print('7')
                            m += 1
                    else:
                        break
                break


        # how to display to the user what was the highest. (postion, boost management, aerial, ground, mechanic)
        # compare the value of the orginal list then corrispond it to the type
        # validates acceptable anwsers

        list_focus = []
        if error == "":
            print("8")
            if position_count == list_mistake_count[len(list_mistake_count) - 1]:
                print("9")
                list_focus.append("Positioning: https://www.youtube.com/watch?v=xiHHbvhRNBU&t=314s")
            if boost_management_count == list_mistake_count[len(list_mistake_count) - 1]:
                print("10")
                list_focus.append("Boost management: https://www.youtube.com/watch?v=eK3DLp-Yjwc")
            if aerial_shots_count == list_mistake_count[len(list_mistake_count) - 1]:
                list_focus.append("Aerial shots: https://www.youtube.com/watch?v=R3k9O-k_XC0&t=280s")
            if ground_shots_count == list_mistake_count[len(list_mistake_count) - 1]:
                list_focus.append("Ground shots: https://www.youtube.com/watch?v=KldJG78wNBU&t=397s")
            if mechanic_count == list_mistake_count[len(list_mistake_count) - 1]:
                print("11")
                list_focus.append("Mechanics: https://www.youtube.com/watch?v=uAOAdvNFpYw")
            # mechanic type
            if mechanic_type == "air dribble":
                list_focus.append(f'air dribble training video: https://www.youtube.com/watch?v=ddEe3t_cKyw')
                list_focus.append(f' Mechanics for ranks: https://www.youtube.com/watch?v=uAOAdvNFpYw')
                print("12")
            elif mechanic_type == "flick" or mechanic_type == "dribble":
                list_focus.append(f'Flick/Dribble training video: https://www.youtube.com/watch?v=576yfVb3MUM&t=184s')
                list_focus.append(f'Mechanics for ranks: https://www.youtube.com/watch?v=uAOAdvNFpYw')
                print("13")
            elif mechanic_type == "mechanic":
                list_focus.append(f"Mechanics for ranks: https://www.youtube.com/watch?v=uAOAdvNFpYw")
                print("14")
            else:
                list_focus.append("Mechanic type doesn't exist, or hasn't been added yet")
                print("15")


        focus_items_print: str = ""
        print("16")
        if error == "":
            focus_items_print: str = focus_items_print + f"Game Title {game_title}\n"
            print("17")
            for i in range(len(list_focus)):
                focus_items_print: str = focus_items_print + f"Focus {list_focus[i]}\n"
                i += 1
                print("18")
            self.textBrowser_TrainingFocus.setText(focus_items_print)
            print(focus_items_print)
            print("19")




        # save the anaylsis's and access pass analysis.
        # with open("game_analysis.csv",'w',newline="") as game_csv:
        #     game_analysis_content = csv.writer(game_csv)
        #     game_csv.write(game_analysis_content)
