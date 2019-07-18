import csv
import sys
import subprocess as sb

from PyQt5 import QtWidgets, uic
import solve_problem


class Ui(QtWidgets.QMainWindow):
    type = 0

    def __init__(self):
        super(Ui, self).__init__()
        w = uic.loadUi('app.ui', self)
        self.w = w
        w.btn_0.clicked.connect(lambda: self.clicked(0))
        w.btn_1.clicked.connect(lambda: self.clicked(1))
        w.btn_2.clicked.connect(lambda: self.clicked(2))
        w.btn_3.clicked.connect(lambda: self.clicked(3))
        w.btn_4.clicked.connect(lambda: self.clicked(4))
        w.btn_5.clicked.connect(lambda: self.clicked(5))
        w.btn_6.clicked.connect(lambda: self.clicked(6))
        w.btn_7.clicked.connect(lambda: self.clicked(7))
        w.bestInstance.clicked.connect(lambda: self.bestinstance())
        w.runButton.clicked.connect(lambda: self.run_algorithm())

    def bestinstance(self):
        print("hi")
        vns_file = csv.DictReader(open("best_parameters.csv"))
        res_ag = 9999999
        ag_file = csv.DictReader(open("fatima.csv"))
        best_algorithme = ''
        best_solution = ''
        val_0 = int(self.w.val_0.value())
        val_1 = int(self.w.val_1.value())
        val_2 = int(self.w.val_2.value())
        name = str(self.w.val_0.value()) + str(self.w.val_1.value()) + str(self.w.val_2.value()) + ".txt"
        for row in vns_file:
            if name + ' ' == row['instance']:
                seq = row['seq']
                x = seq.split(',')
                res_vns = int(x[-1])
                vns_all = row
                print(res_vns)

        for row in ag_file:
            if name == row['probleme']:
                res_ag = int(row['makespan'])
                ag_all = row
                print(res_ag)

        if res_ag < res_vns :
            best_algorithme = 'AG'
            best_solution = res_ag
            best_parameters = ag_all
            best_parameters["sequence"] = ""
        else:
            best_algorithme = 'VNS'
            best_solution = res_vns
            best_parameters = vns_all
            best_parameters["seq"] = ""
        print(best_algorithme, best_solution, best_parameters)
        self.w.label_resultat.setText(best_algorithme + str(best_parameters))
        self.w.timeField.display(best_solution)

    def clicked(self, id):
        self.type = id
        print(type)
        print('Button {0} clicked'.format(id))
        if (id == 5):
            self.w.label_8.setText("initialisation")
            self.w.label_9.setText("limite stagnation")
            self.w.label_10.setText("strategie de recherche")
        if (id == 4):
            self.w.label_8.setText("taille population")
            self.w.label_9.setText("taille generation")
            self.w.label_10.setText("probabilite mutation")

    def run_algorithm(self):
        val_0 = int(self.w.val_0.value())
        val_1 = int(self.w.val_1.value())
        val_2 = int(self.w.val_2.value())
        val_3 = int(self.w.val_3.value())
        val_4 = int(self.w.val_4.value())
        val_5 = int(self.w.doubleSpinBox.value())
        print(val_0, val_1, val_2)
        print(val_5)
        # get the file name for NEH amelioree and CDS
        file_name = str(self.w.val_0.value()) + str(self.w.val_1.value()) + str(self.w.val_2.value()) + ".txt"
        open("instance/" + file_name, 'r')
        # self.w.text.append("CLicked with values %d, %d , %d " % (val_0, val_1, val_2))
        if self.type == 0:  # branch and bound
            pass
        elif self.type == 1:  # NEH
            sequence2 = sb.check_output(['neh.exe', 'instance/' + str(file_name)])
            sequence = sequence2.decode("utf-8")
            x = sequence.split(",")
            makespan = x[self.w.val_2.value()]
            pass
        elif self.type == 2:  # NEH Amelioree
            a = 'NehAmelioree.exe instance/' + str(file_name)
            sequence = sb.getoutput(str(a))
            # get the makespan from the sequence string
            x = sequence.split(",")
            makespan = x[self.w.val_2.value()]
        elif self.type == 3:  # CDS
            a = 'cds.exe instance/' + str(file_name)
            sequence = sb.getoutput(str(a))
            # get the makespan from the sequence string
            x = sequence.split(",")
            makespan = x[self.w.val_2.value()]
        elif self.type == 4:  # Algorithme genetique
            sequence, makespan = solve_problem.solve_benchmark_problem(val_0, val_2, val_1, val_3, val_4, val_5)
        elif self.type == 5:  # VNS

            sequence2 = sb.check_output(['neh.exe', 'instance/' + str(file_name)])
            sequence3 = sb.check_output(
                ['vns.exe', 'instance/' + str(file_name), str(val_0), sequence2.decode("utf-8"), "0", str(val_1),
                 str(int(val_2))])
            sequence = sequence3.decode("utf-8")
            x = sequence.split(",")
            makespan = x[self.w.val_2.value()]
        elif self.type == 6:  # Hyper Heuristqiue
            res = sb.getoutput('python hyper.py' + ' instance/' + file_name)
            print(res)
            res = res.split(',')
            sequence = res[:-1]
            # Convert them to a list of int
           # sequence = list(map(int, sequence))
            makespan = res[-1]
        elif self.type == 7:  # Palmer
            res = sb.getoutput('python Palmer_s_Heurtistic.py' +
                               ' instance/' + file_name).split(',')
            sequence = res[:-1]
            # Convert them to a list of int
            sequence = list(map(int, sequence))
            makespan = res[-1]

        print(sequence, makespan)
        self.w.label_resultat.setText(str(sequence))
        self.w.timeField.display(makespan)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()
    # sys.exit()
