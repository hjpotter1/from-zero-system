from array import array
from flask import Flask, request
import os
import json
import SqliteUtil as DBUtil

app = Flask(__name__, template_folder='../front-end',
            static_folder='../front-end', static_url_path='')


@app.route('/hi')
def hi():
    return 'hi~'


# api接口前缀
apiPrefix = '/api/v1/'

##################  Staff接口  ##################


@app.route(apiPrefix + 'updateStaff', methods=['POST'])
def updateStaff():
    data = request.get_data(as_text=True)
    print("后端数据：", data)
    re = DBUtil.addOrUpdateStaff(data)
    return json.dumps(re)


@app.route(apiPrefix + 'getStaffList/<int:job>')
def getStaffList(job):
    # [('1', '1', '1', '1', '1'), ('1', '1', '2', '3', '4'), ...] 二维数组
    array = DBUtil.getStaffList(job)
    jsonStaffs = DBUtil.getStaffsFromData(array)
    print("后端数据jsonStaffs:", jsonStaffs)
    return json.dumps(jsonStaffs)


@app.route(apiPrefix + 'deleteStaff/<int:id>')
def deleteStaff(id):
    print("delete")
    re = DBUtil.deleteStaff(id)
    return re


@app.route(apiPrefix + 'searchStaff_3')
def searchStaff_3():
    data = request.args.get('where')
    print('searchStaff_3', data)
    where = json.load(data)
    array = DBUtil.searchStaff_3(where)
    jsonStaffs = DBUtil.getStaffsFromData_3(array)
    re = json.dumps(jsonStaffs)
    return re


if __name__ == "__main__":
    app.run(debug=True, port=5001)
