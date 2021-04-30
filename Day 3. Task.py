from blockdiag import parser, builder, drawer


source = """
        blockdiag {
            default_shape = roundedbox
            A [label = "Welcome to Treasure Island.\nYour mission is to find the treasure"]
            A [width = 230]
            B [label = "left or\nright?"]
            B [shape = flowchart.condition]
            C [label = "swim or\nwait?"]
            C [shape = flowchart.condition]
            D [label = "Which door?"]
            D [shape = flowchart.condition]
            E [label = "You Win!"]
            group vertical {
                orientation = portrait
                A -> B; 
                B -> C [label = "Left", fontsize = 8];
                C -> D [label = "Wait", fontsize = 8];
                D -> E [label = "Yellow", fontsize = 8];
                color = "#FFFFFF";
                }
            F [label = "Game Over."]
            G [label = "Game Over."]
            H [label = "Game Over."]
            I [label = "Game Over."]
            B -> F [label = "Right", fontsize = 8];
            C -> G [label = "Swim", fontsize = 8];
            I <- D [label = "Red", fontsize = 8];
            D -> H [label = "Blue", fontsize = 8];
        }
        """
tree = parser.parse_string(source)
diagram = builder.ScreenNodeBuilder.build(tree)
draw = drawer.DiagramDraw('PNG', diagram, filename="Day3_task.png")
draw.draw()
draw.save()
