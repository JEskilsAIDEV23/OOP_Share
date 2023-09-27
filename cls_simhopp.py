class Simhopp:
    def __init__(self, domare = 0, degree = 0, given_points =[]):
        self.__domare = domare
        self.__degree = degree
        self.__given_points = given_points

        while True:
            if domare < 3:
                #print('Fel antal domare: ')
                domare = int(input('Antal domare: '))
                self.__domare = domare
                continue
            else:
                break 

        while True:
            if degree < 1 or degree > 5:
               # print('Fel svårighetsgrad: ')
                degree = int(input('1-5: '))
                self.__degree = degree
                continue
            else:
                break

        if given_points == [] or len(given_points) != domare:
            given_points.clear()
            n = 1
            while n <= domare:
                give_p = float(input(f'Judge {n}: '))
                if give_p < 0 or give_p > 10:
                    continue
                if give_p > 0 or give_p <= 10:
                    given_points.append(give_p)  
                    n +=1 
                    continue
                else:
                    break
    
    def get_domare(self):
        return self.__domare      

    def get_given_points(self):
        return self.__given_points

    def get_degree(self):
        return self.__degree
    
    def points_awarded(self, given_points, degree):
         point_calc = given_points
         point_calc.sort()
         del point_calc[0]
         del point_calc[-1]

         point_award = sum(point_calc)/len(point_calc)*3*degree

         return point_award

         


    
    

