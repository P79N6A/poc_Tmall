!function(){if(!(KISSY.UA.ie&&KISSY.UA.ie<8)){var r=/\w*.(?:pre.taobao.com|daily.taobao.net)/.test(location.href)?"/src/":"//g.alicdn.com/searchInteraction/keyword-brand-pc/0.0.6/";KISSY.config({packages:[{name:"keywordBrandPC",path:r,ignorePackageNameInUri:!0,debug:!0,combine:!1}]}),KISSY.config("modules",{"keywordBrandPC/_0":{requires:["keywordBrandPC/p/keyword-brand/index.css","json","node","overlay","keywordBrandPC/_1","cookie","tbc/mini-login/2.2.9/index"]},"keywordBrandPC/_1":{requires:["json"]},"keywordBrandPC/p/keyword-brand/index":{alias:"keywordBrandPC/_0"},"keywordBrandPC/p/keyword-brand/mtop":{alias:"keywordBrandPC/_1"}}),window.initKeywordBrandhb=function(r){r.status&&"show"===r.status&&r.data&&KISSY.use("keywordBrandPC/p/keyword-brand/",function(a,n){n.init(r.data)})}}}();