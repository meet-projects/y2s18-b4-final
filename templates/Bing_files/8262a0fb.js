var Identity=Identity||{};(function(n,t,i,r,u,f,e){function c(){h||(o.style.display="block",h=!0,t.fire("identityHeaderShown"))}var h=!1;e.wlProfile=function(){var r=sj_cook.get,u="WLS",t=r(u,"N"),i=r(u,"C");return t&&i&&e.wlImgSm&&e.wlImgLg?{displayName:n(t.replace(/\+/g," ")),name:n(t.replace(/\+/g," ")),img:e.wlImgSm.replace(/\{0\}/g,f(i)),imgL:e.wlImgLg.replace(/\{0\}/g,f(i)),idp:"WL"}:null};e.headerLoginMode=0;e.popupAuthenticate=function(n,i,r){var o,u,h,c,v=sb_gt(),l=Math.floor(v/1e3).toString(),s="ct",a=new RegExp("([?&])"+s+"=.*?(&|$)","i");return n.toString()==="WindowsLiveId"&&(o=e.popupLoginUrls,u=o[n],u=u.match(a)?u.replace(a,"$1"+s+"="+l+"$2"):u+"?"+s+"="+l,e.popupLoginUrls.WindowsLiveId=u),(o=e.popupLoginUrls)&&(u=o[n]+(i?"&perms="+f(i):"")+(r?"&src="+f(r):""))&&(h=e.pop(u))&&(c=setInterval(function(){h.closed&&(t.fire("id:popup:close"),clearInterval(c))},100))};e.pop=function(n){return r.open(n,"idl","location=no,menubar=no,resizable=no,scrollbars=yes,status=no,titlebar=no,toolbar=no,width=1000,height=620")};var o=u("id_h"),s=u("id_l"),l="click";t.bind("onP1",function(){setTimeout(function(){var u,n;o&&s&&(sj_jb("Blue/BlueIdentityDropdownRedirect_c",0,o,"mouseover",s,l,s,"focus"),i(s,l,function(n){e.hdrClk=n}));o&&(u="BNCenter",r[u]=r[u]||{},n=r[u],n.hbncl?c():(n.ihrt=sb_gt(),t.bind("BNCHCLoaded",c),sb_st(function(){h||(n.ssv=!0);c()},n.sams||500)))},50)},1)})(decodeURIComponent,sj_evt,sj_be,_w,_ge,encodeURIComponent,Identity,_G.RTL)