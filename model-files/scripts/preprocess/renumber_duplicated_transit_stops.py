import csv, glob, os, re, sys, traceback
from math import pow, sqrt
from collections import defaultdict

from Wrangler import setupLogging, Network, TransitLine, TransitNetwork, TransitAssignmentData, WranglerLogger
from dataTable import DataTable, FieldType
import numpy as np
import math
os.chdir("trn")
setupLogging(infoLogFilename=None, debugLogFilename="transit_duplicated_stops_updated_to_nodes.txt", logToConsole=True)
net = TransitNetwork(modelType="TravelModelOne", modelVersion=1.0)

net.parseFile(fullfile="transit_converted_2.lin",insert_replace=True)

for lineidx in xrange(len(net.lines)-1, -1, -1):
    if not isinstance(net.lines[lineidx],TransitLine): continue
    if net.lines[lineidx].hasDuplicateStops():
        _stop_to_idx = {}
        _stop_list   = []
        all_nodes=net.lines[lineidx].listNodeIds(ignoreStops=False)
        for node in all_nodes:
            node_num=node             
            if node_num not in _stop_to_idx: 
                _stop_to_idx[node_num] = []
            _stop_to_idx[node_num].append(len(_stop_list))  
            _stop_list.append(np.int(node_num))
        for node_num in _stop_to_idx.keys():
            if len(_stop_to_idx[node_num]) == 1: continue #just one occurence
            if _stop_to_idx[node_num] == [0,len(_stop_list)-1]: continue
            if _stop_to_idx[node_num][0] == 0:
                for elem in _stop_to_idx[node_num][1:]:
                    WranglerLogger.info("Updated all but first instance of the duplicated stop {} on Line: {} to be a node".format(_stop_list[elem],net.lines[lineidx].name))
                    _stop_list[elem] = -abs(np.int(_stop_list[elem]))
            else:
                for elem in _stop_to_idx[node_num][:-1]:
                    WranglerLogger.info("Updated all but last instance of the duplicated stop {} on Line: {} to be a node".format(_stop_list[elem],net.lines[lineidx].name))
                    _stop_list[elem] = -abs(np.int(_stop_list[elem]))
                

        net.lines[lineidx].setNodes(_stop_list)
            
net.write(name='transit_duplicated_stops_removed_new', writeEmptyFiles=False, suppressQuery=True, suppressValidation=True, cubeNetFileForValidation=None)