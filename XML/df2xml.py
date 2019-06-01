#
# This lib turn a pandas dataframe in a xml metadata file
# The class will turn each column name as a child of the root, and will create N sub childs to every statistic metric: mean, max, min
# Author: Lucas Hideki Ueda | Copyright 2019
#

import pandas as pd
from pandas.api.types import is_numeric_dtype
import xml.etree.ElementTree as ET
import xml.dom.minidom as dom

class XMLGenerator():
    
    """
    A class that allow you to create a metadata in XML file from an Pandas DataFrame

    ...

    Attributes
    ----------
    root : obj
        a root of the XML file
        
    Methods
    ----------
    getMeta()
        Prints the dataset name
        
    to_dataframe()
        Return a Pandas DataFrame with the XML file childs tag, attrib and text
    
    getDescription(variable)
        Get the text associate to the variable input, that literally is the variable explanation
    
    describe()
        Return a description of the XML file

    """

    df = None
    pretty_xml = None
    
    def __init__(self, root = 'root'):
        
        """
        Constructor default method
        
        Parameters
        ----------
        dataset : str
            a formatted string the same of the dataset choosen name
            
        """
        
        self.root = ET.Element(root)

    def __str__(self):
        
        """
        Print default method
                
        Return
        ----------
        String
            a formatted string with the XML file
            
        """
            
        if(self.pretty_xml != None):
            return self.pretty_xml
        else:
            return 'XML file is undefined'
    
    def getXML(self):
        
        """
        Get method to return the object
                
        Return
        ----------
        obj
            the root of XML file 
            
        """
        
        return self.root
    
    def to_xml(self, dataframe, descriptions= None):
        
        """
        Method to transform a inputed dataframe to xml file
                
        Parameters
        ----------
        dataframe : pandas.Dataframe
            a dataframe to turn in a xml file
        
        Return
        ----------
        obj
            return self.root
            
        """
        
        self.df = dataframe.copy()
        
        for v in dataframe.columns:
            
            df_aux = dataframe[v]
            
            child = ET.SubElement(self.root, 'variable')
            child.set('name',v)
            
            if(is_numeric_dtype(df_aux)):
                b_bound = df_aux.min()
                u_bound = df_aux.max()
                mean = df_aux.mean()
                p25 = df_aux.quantile(.25)
                p75 = df_aux.quantile(.75)
                p90 = df_aux.quantile(.90)
           
                subchild1 = ET.SubElement(child,'Minimum_value')
                subchild1.text = str(b_bound)
                
                subchild2 = ET.SubElement(child,'Maximum_value')
                subchild2.text = str(u_bound)
                
                subchild3 = ET.SubElement(child,'Mean_value')
                subchild3.text = str(mean)
                
                subchild4 = ET.SubElement(child,'Percentile_25th')
                subchild4.text = str(p25)
                
                subchild5 = ET.SubElement(child,'Percentile_75th')
                subchild5.text = str(p75)
                
                subchild6 = ET.SubElement(child,'Percentile_90th')
                subchild6.text = str(p90)
               
        return self.root
    
    def save(self, save_name):
        
        """
        Method that save the root as an XML file with pretty print
        
        Parameters
        ----------
        save_name : str
            the name of the file to be saved
        
        Return
        ----------
        String
            Return a message of sucessful or not
            
        """
        try:
            
            string_root = ET.tostring(self.root,encoding='utf8').decode('utf8')

            dom_root = dom.parseString(string_root)

            metadata = dom_root.toprettyxml()

            self.pretty_xml = metadata
 
            save_name = save_name + '.xml'

            xml_file = open(save_name,'w')

            xml_file.write(metadata)
            
            return f'The XML file {save_name} was sucessfully created! '
        
        except:
            
            return f'''Save method didn't work'''
    
    
    