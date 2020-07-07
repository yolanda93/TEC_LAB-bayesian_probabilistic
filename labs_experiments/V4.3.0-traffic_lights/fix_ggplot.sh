
auxfile='auxfile'

#ggplot files
ggplotutils='../../../lib/python3.6/site-packages/ggplot/utils.py'
ggplotsmoothers='../../../lib/python3.6/site-packages/ggplot/stats/smoothers.py'

cat $ggplotutils | sed -e 's/pd.tslib.Timestamp/pd.Timestamp/g'  > $auxfile
mv $auxfile $ggplotutils


cat $ggplotsmoothers | sed -e 's/pandas.lib import Timestamp/pandas import Timestamp/g'  > $auxfile
mv $auxfile $ggplotsmoothers

cat $ggplotsmoothers | sed -e 's/pd.tslib.Timestamp/pd.Timestamp/g'  > $auxfile
mv $auxfile $ggplotsmoothers
