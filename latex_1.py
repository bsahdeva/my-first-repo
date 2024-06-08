import manim as bb

class MyScene(bb.Scene):
    def construct(self):
        font_size = 20      

        line1 = bb.Text("A facility is filling several 1500 liter containers with water.", font_size=font_size * 0.75)
        line2 = bb.Text("In order to make the most optimal use of space, the facility wants each container to be completely full.", font_size=font_size * 0.75)
        line3 = bb.Text("Every hour, the volume of water within the container triples.", font_size=font_size * 0.75)
        line4 = bb.Text("After 3 hours, there are 50 milliliters of water within the container.", font_size=font_size * 0.75)
        line5 = bb.Text("To the nearest hundredth, how many hours will it take for one container to be completely full?", font_size=font_size * 0.75)
        
        self.add(bb.VGroup(line1,
                           line2,
                           line3,
                           line4,
                           line5).arrange(bb.DOWN).shift(bb.RIGHT * 2))


        step1 = bb.MathTex(r"\frac{\mathrm{d}y}{\mathrm{d}t} = 3y",
                           font_size=font_size)
        step2 = bb.MathTex(r"\frac{\mathrm{d}y}{y} = 3\mathrm{d}t",
                           font_size=font_size)
        step3 = bb.MathTex(r"\frac{1}{y}\mathrm{d}y} = 3\mathrm{d}t",
                           font_size=font_size)
        step4 = bb.MathTex(r"\int \frac{1}{y}\mathrm{d}y} = \int 3\mathrm{d}t",
                           font_size=font_size)
        step5 = bb.MathTex(r"\ln{|y|} + C_1 = 3t + C_2",
                           font_size=font_size)
        step6 = bb.MathTex(r"\ln{|y|} = 3t + C_3",
                           font_size=font_size)
        step7 = bb.MathTex(r"y = e^{3t + C_2}",
                           font_size=font_size)
        step8 = bb.MathTex(r"y = Ce^{3t}",
                           font_size=font_size)
        step9 = bb.MathTex(r"0.05 = Ce^{3 \cdot 3}",
                           font_size=font_size)
        
        self.add(bb.VGroup(step1, 
                           step2, 
                           step3, 
                           step4, 
                           step5,
                           step6,
                           step7,
                           step8,
                           step9).arrange(bb.DOWN).shift(bb.LEFT * 4))