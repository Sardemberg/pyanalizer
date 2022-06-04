import json
import plotly.express as px
import plotly.graph_objects as go


class ShowChart:
    # def __init__(self):
    # self.cities_ceara = json.load(open('ui/geojson/file.json','r'))

    # def show(self):
    # print(self.cities_ceara['features'][1])
    def chartProblems(self):

        # data = dict(

        #     character=["Problemas", "Energia", "Cabo", "Manutenção",
        #                "Tempestade", "Sobrecarga", "Problemas no sistema", "Crato", "Juazeiro do Norte", "Barbalha", "Exu", "Campo Sales"],
        #     parent=["", "Problemas", "Problemas", "Problemas",
        #             "Problemas", "Problemas", "Problemas", "Manutenção", "Cabo", "Tempestade", "Sobrecarga", "Problemas no sistema"],
        #     value=[100, 5, 10, 15, 20, 25, 25, 10, 10, 10, 10, 10])

        # fig = px.sunburst(
        #     data,
        #     branchvalues='total',
        #     names='character',
        #     parents='parent',
        #     values='value',
        # )
        # fig.show()

        # fig = go.Figure(go.Sunburst(
        #     ids=[
        #         "North America", "Europe", "Australia", "North America - Football", "Soccer",
        #         "North America - Rugby", "Europe - Football", "Rugby",
        #         "Europe - American Football", "Australia - Football", "Association",
        #         "Australian Rules", "Autstralia - American Football", "Australia - Rugby",
        #         "Rugby League", "Rugby Union"
        #     ],
        #     labels=[
        #         "North<br>America", "Europe", "Australia", "Football", "Soccer", "Rugby",
        #         "Football", "Rugby", "American<br>Football", "Football", "Association",
        #         "Australian<br>Rules", "American<br>Football", "Rugby", "Rugby<br>League",
        #         "Rugby<br>Union"
        #     ],
        #     parents=[
        #         "", "", "", "North America", "North America", "North America", "Europe",
        #         "Europe", "Europe", "Australia", "Australia - Football", "Australia - Football",
        #         "Australia - Football", "Australia - Football", "Australia - Rugby",
        #         "Australia - Rugby"
        #     ],
        # ))
        # fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

        # fig.show()
        fig = go.Figure(
            go.Sunburst(

                ids=[
                    "Problemas", "Fio", "Energia", "Manutenção", "Jua-fio", "crato-frio", "barbalha-fio", "Jua-energia", "crato-Manutenção"
                ],
                labels=[
                    "Problemas", "Fio", "Energia", "Manutenção", "Jua", "crato", "barbalha", "Jua-energia", "crato-Manutenção"
                ],
                parents=[

                    "", "Problemas", "Problemas", "Problemas", "Fio", "Fio", "Fio", "Energia", "Manutenção"
                ],
                values=[100, 30, 50, 20, 5, 15, 5, 20, 15],
                branchvalues="total",
                # hoverlabel=['a', 'b', 'c', 'd', "e", "f", "g", "j", "k"],

            ))
        fig.update_traces(hoverinfo="label+text+value")
        fig.update_layout(


            title_text="Gráfico de problemas",
        )

        fig.show()
