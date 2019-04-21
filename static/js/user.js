var areaData = address;
var $form;
var form;
var $;
layui.config({
	base : "/static/js/"
}).use(['form','layer','upload','laydate'],function(){
	form = layui.form();
	var layer = parent.layer === undefined ? layui.layer : parent.layer;
		$ = layui.jquery;
		$form = $('form');
		laydate = layui.laydate;
        loadProvince(); //加载省信息

    //添加验证规则
    form.verify({
        oldPwd : function(value, item){
            if(value != "123456"){
                return "密码错误，请重新输入！";
            }
        },
        newPwd : function(value, item){
            if(value.length < 6){
                return "密码长度不能小于6位";
            }
        },
        confirmPwd : function(value, item){
            if(!new RegExp($("#oldPwd").val()).test(value)){
                return "两次输入密码不一致，请重新输入！";
            }
        }
    })

    //判断是否修改过用户信息，如果修改过则填充修改后的信息
    if(window.sessionStorage.getItem('userInfo')){
        var userInfo = JSON.parse(window.sessionStorage.getItem('userInfo'));
        var citys;
        $(".realName").val(userInfo.realName); //用户名
        $(".userSex input[value="+userInfo.sex+"]").attr("checked","checked"); //性别
        $(".userPhone").val(userInfo.userPhone); //手机号
        $(".userBirthday").val(userInfo.userBirthday); //出生年月
        $(".userAddress select[name='province']").val(userInfo.province); //省
        //填充省份信息，同时调取市级信息列表
        var value = userInfo.province;
        var d = value.split('_');
        var code = d[0];
        var count = d[1];
        var index = d[2];
        if (count > 0) {
            loadCity(areaData[index].mallCityList);
            citys = areaData[index].mallCityList
        } else {
            $form.find('select[name=city]').attr("disabled","disabled");
        }
        $(".userAddress select[name='city']").val(userInfo.city); //市
        //填充市级信息，同时调取区县信息列表
        var value = userInfo.city;
        var d = value.split('_');
        var code = d[0];
        var count = d[1];
        var index = d[2];
        if (count > 0) {
            loadArea(citys[index].mallAreaList);
        } else {
            $form.find('select[name=area]').attr("disabled","disabled");
        }
        $(".userAddress select[name='area']").val(userInfo.area); //区
        for(key in userInfo){
            if(key.indexOf("like") != -1){
                $(".userHobby input[name='"+key+"']").attr("checked","checked");
            }
        }
        $(".email").val(userInfo.email); //用户邮箱
        $(".myself").val(userInfo.myself); //自我评价
        form.render();
    }

     //提交个人资料
    form.on("submit(changeUser)",function(data){
    	var index = layer.msg('提交中，请稍候',{icon: 16,time:false,shade:0.8});
        //将填写的用户信息存到session以便下次调取
        var key,userInfoHtml = '';
        userInfoHtml = {
            'realName' : $(".realName").val(),
            'sex' : data.field.sex,
            'userPhone' : $(".userPhone").val(),
            'userBirthday' : $(".userBirthday").val(),
            'province' : data.field.province,
            'city' : data.field.city,
            'area' : data.field.area,
            'email' : $(".userEmail").val(),
            'myself' : $(".myself").val()
        };
        for(key in data.field){
            if(key.indexOf("like") != -1){
                userInfoHtml[key] = "on";
            }
        }
        window.sessionStorage.setItem("userInfo",JSON.stringify(userInfoHtml));
        setTimeout(function(){
            layer.close(index);
            layer.msg("提交成功！");
        },2000);
    	return false; //阻止表单跳转。如果需要表单跳转，去掉这段即可。
    })

    // //提交个人资料
    // form.on("submit(changeUser)",function(data){
    // 	var index = layer.msg('提交中，请稍候',{icon: 16,time:false,shade:0.8});
    //     //将填写的用户信息存到session以便下次调取
    //     // var key,userInfoHtml = '';
    //     // userInfoHtml = {
    //     //     'realName' : $(".realName").val(),
    //     //     'sex' : data.field.sex,
    //     //     'userPhone' : $(".userPhone").val(),
    //     //     'userBirthday' : $(".userBirthday").val(),
    //     //     'province' : data.field.province,
    //     //     'city' : data.field.city,
    //     //     'area' : data.field.area,
    //     //     'userEmail' : $(".userEmail").val(),
    //     //     'myself' : $(".myself").val()
    //     // };
    //     // for(key in data.field){
    //     //     if(key.indexOf("like") != -1){
    //     //         userInfoHtml[key] = "on";
    //     //     }
    //     // }
    //      var _self = $(this),
    //         $jsEditUserForm = $('#jsEditUserForm')
    //         verify = verifySubmit(
    //         [
    //             {id: '#nick_name', tips: Dml.Msg.epNickName, require: true}
    //         ]
    //     );
    //     if(!verify){
    //        return;
    //     }
    //     $.ajax({
    //         cache: false,
    //         type: 'post',
    //         dataType:'json',
    //         url:"/users/info/",
    //         data:$jsEditUserForm.serialize(),
    //         async: true,
    //         beforeSend:function(XMLHttpRequest){
    //             _self.val("保存中...");
    //             _self.attr('disabled',true);
    //         },
    //         success: function(data) {
    //             if(data.nick_name){
    //                 _showValidateError($('#nick_name'), data.nick_name);
    //             }else if(data.birday){
    //                _showValidateError($('#birth_day'), data.birday);
    //             }else if(data.address){
    //                _showValidateError($('#address'), data.address);
    //             }else if(data.status == "failure"){
    //                  Dml.fun.showTipsDialog({
    //                     title: '保存失败',
    //                     h2: data.msg
    //                 });
    //             }else if(data.status == "success"){
    //                 Dml.fun.showTipsDialog({
    //                     title: '保存成功',
    //                     h2: '个人信息修改成功！'
    //                 });
    //                 setTimeout(function(){window.location.href = window.location.href;},1500);
    //             }
    //         },
    //         complete: function(XMLHttpRequest){
    //             _self.val("保存");
    //             _self.removeAttr("disabled");
    //         }
    //     });
    //
    //
    //     //window.sessionStorage.setItem("userInfo",JSON.stringify(userInfoHtml));
    //     setTimeout(function(){
    //         layer.close(index);
    //         layer.msg("提交成功！");
    //     },2000);
    // 	return false; //阻止表单跳转。如果需要表单跳转，去掉这段即可。
    // })

    //修改密码
    form.on("submit(changePwd)",function(data){
    	var index = layer.msg('提交中，请稍候',{icon: 16,time:false,shade:0.8});
        setTimeout(function(){
            layer.close(index);
            layer.msg("密码修改成功！");
            $(".pwd").val('');
        },2000);
    	return false; //阻止表单跳转。如果需要表单跳转，去掉这段即可。
    })

})

//加载省数据
function loadProvince() {
    var proHtml = '';
    for (var i = 0; i < areaData.length; i++) {
        proHtml += '<option value="' + areaData[i].provinceCode + '_' + areaData[i].mallCityList.length + '_' + i + '">' + areaData[i].provinceName + '</option>';
    }
    //初始化省数据
    $form.find('select[name=province]').append(proHtml);
    form.render();
    form.on('select(province)', function(data) {
        $form.find('select[name=area]').html('<option value="">请选择县/区</option>');
        var value = data.value;
        var d = value.split('_');
        var code = d[0];
        var count = d[1];
        var index = d[2];
        if (count > 0) {
            loadCity(areaData[index].mallCityList);
        } else {
            $form.find('select[name=city]').attr("disabled","disabled");
        }
    });
}
//加载市数据
function loadCity(citys) {
    var cityHtml = '<option value="">请选择市</option>';
    for (var i = 0; i < citys.length; i++) {
        cityHtml += '<option value="' + citys[i].cityCode + '_' + citys[i].mallAreaList.length + '_' + i + '">' + citys[i].cityName + '</option>';
    }
    $form.find('select[name=city]').html(cityHtml).removeAttr("disabled");
    form.render();
    form.on('select(city)', function(data) {
        var value = data.value;
        var d = value.split('_');
        var code = d[0];
        var count = d[1];
        var index = d[2];
        if (count > 0) {
            loadArea(citys[index].mallAreaList);
        } else {
            $form.find('select[name=area]').attr("disabled","disabled");
        }
    });
}
//加载县/区数据
function loadArea(areas) {
    var areaHtml = '<option value="">请选择县/区</option>';
    for (var i = 0; i < areas.length; i++) {
        areaHtml += '<option value="' + areas[i].areaCode + '">' + areas[i].areaName + '</option>';
    }
    $form.find('select[name=area]').html(areaHtml).removeAttr("disabled");
    form.render();
    form.on('select(area)', function(data) {});
}
