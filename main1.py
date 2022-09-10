from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

Window.size=(500,700)
Builder.load_file('main1.kv')

class MyLayout(Widget):

    def clear(self):
        self.ids.calc_input.text='0'
    def btnPressNum(self, numPress):
        prior=self.ids.calc_input.text;
        print("numPress: ", numPress);
        print("prior:", prior)
        if(prior=="0"):
            self.ids.calc_input.text=''
            self.ids.calc_input.text = f'{numPress}'
        else:
            self.ids.calc_input.text = f'{prior}{numPress}';

    def btnSign(self,sign):
        prior = self.ids.calc_input.text;
        print("prior:", prior)
        if (prior == "0" or prior == "E"):
            pass
        else:
            self.ids.calc_input.text = f'{prior}{sign}'

    def btnDot(self):
        prior = self.ids.calc_input.text;
        print("prior:", prior)

        #validate dot in last digit in sign +
        numList=prior.split("+")
        if( "." not in  numList[-1]):
            self.ids.calc_input.text = f'{prior}.'

        # validate dot in last digit in sign -
        numList = prior.split("-")
        if ("." not in numList[-1]):
            self.ids.calc_input.text = f'{prior}.'

        # validate dot in last digit in sign *
        numList = prior.split("-")
        if ("." not in numList[-1]):
            self.ids.calc_input.text = f'{prior}.'

        # validate dot in last digit in sign /
        numList = prior.split("-")
        if ("." not in numList[-1]):
            self.ids.calc_input.text = f'{prior}.'

    def btnRemove(self):
        prior = self.ids.calc_input.text;
        print("prior:", prior)
        prior = prior[:-1]
        self.ids.calc_input.text = f'{prior}'

    def btnPosNeg(self):
        prior = self.ids.calc_input.text;
        print("prior:", prior)
        prior=(int(prior))*(-1)
        self.ids.calc_input.text = f'{prior}'

    def btnEquals(self):
        prior=self.ids.calc_input.text;
        print("prior: ",prior)

        answer = eval(prior)
        self.ids.calc_input.text=str(answer)
        """
        answer = 0.0;
        if "+" in prior:
            numList=prior.split("+")
            print("numList ", numList)
            print("numList[:-1]:", numList[:-1])
            print("numList[-1]:", numList[-1])
            answer=0;
            for number in numList:
                answer=answer+float(number);
            self.ids.calc_input.text=f'{answer}';
        """

class CalculatorApp(App):
    def build(self):
        return MyLayout();

if __name__ =='__main__':
    CalculatorApp().run();