cd ..
cd ..
mkdir logs

rem ############  PARAMETERS  ############
:: Set the path
call CTRAMP\runtime\SetPath.bat

set HOST_IP=set_by_RuntimeConfiguration.py

rem ############  JPPF DRIVER  ############
start "Node 0" java -server -Xmx128m -Dlog4j.configuration=log4j-node0.xml -Djppf.config=jppf-node0.properties org.jppf.node.NodeLauncher
