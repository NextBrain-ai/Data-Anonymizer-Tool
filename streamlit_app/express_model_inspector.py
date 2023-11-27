import plotly.subplots as sp
import plotly.graph_objs as go

from DataSynthesizer.ModelInspector import ModelInspector 
from pandas import DataFrame

#Workaround for issues with DataSynthetizer 
#graphs incompatible with streamlit 
class ExpressModelInspector(ModelInspector):
    
    def __init__(self, private_df: DataFrame, synthetic_df: DataFrame, attribute_description):
      super().__init__(private_df, synthetic_df, attribute_description)   
    
    def compare_histograms(self, attribute):
        datatype = self.attribute_description[attribute]['data_type']
        is_categorical = self.attribute_description[attribute]['is_categorical']    
        if datatype == 'DateTime':
            return None
        elif datatype == 'String' and not is_categorical:
            return None
        elif attribute in self.candidate_keys:
            return None
        else:
            if is_categorical:
                dist_priv = self.private_df[attribute].value_counts(normalize=True).sort_index()
                dist_synt = self.synthetic_df[attribute].value_counts(normalize=True).sort_index()    
                fig = sp.make_subplots(rows=1, cols=2, subplot_titles=('Private', 'Synthetic'))   
                fig.add_trace(go.Bar(x=dist_priv.index, y=dist_priv.values, name='Private'), row=1, col=1)    
                fig.add_trace(go.Bar(x=dist_synt.index, y=dist_synt.values, name='Synthetic'), row=1, col=2)    
                fig.update_layout(title=f'Histogram Comparison for {attribute}', barmode='group',
                                  legend=dict(x=0, y=1, traceorder='normal', orientation='h'))    
            else:
                fig = sp.make_subplots(rows=1, cols=2, subplot_titles=('Private', 'Synthetic'))   
                fig.add_trace(go.Histogram(x=self.private_df[attribute].dropna(), opacity=0.7, name='Private'), row=1, col=1)   
                fig.add_trace(go.Histogram(x=self.synthetic_df[attribute].dropna(), opacity=0.7, name='Synthetic'), row=1, col=2)   
                fig.update_layout(title=f'Histogram Comparison for {attribute}', legend=dict(x=0, y=1, traceorder='normal', orientation='h'))   
        fig['layout'].update(height=600, width=1400)
        return fig
