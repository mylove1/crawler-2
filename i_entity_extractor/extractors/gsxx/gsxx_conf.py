# coding=utf8
business_status_map = {
    u"存续": u"存续", u"存续（在营、开业、在册）": u"存续",
    u"吊销，未注销": u"吊销", u"在营（开业）企业": u"在业", u"存活": u"存续", u"该企业已登记成立": u"在业", u"开业": u"存续", u"吊销": u"吊销",
    u"在业": u"在业",
    u"注销": u"注销", u"已注销": u"注销", u"登记成立": u"在业", u"吊销企业": u"吊销", u"该企业已注销": u"注销", u"该企业已吊销": u"吊销",
    u"在营（开业）": u"在业",
    u"确立": u"在业", u"已核准名称": u"在业", u"营业": u"在业", u"内资存活": u"存活", u"已登记": u"在业", u"存续(在营、开业、在册)": u"存续",
    u"已变更": u"迁出",
    u"吊销未注销": u"吊销", u"内资注销": u"注销", u"迁出": u"迁出", u"已成立": u"在业", u"注销企业": u"注销", u"变更": u"迁出", u"内资吊销": u"吊销",
    u"非正常户": u"吊销",
    u"已开业": u"在业", u"已吊销": u"吊销", u"在册": u"存续", u"存在": u"存续", u"异地迁入": u"迁入", u"新增": u"迁入", u"开业/正常经营": u"在业",
    u"正常": u"存续",
    u"变更登记中": u"迁出", u"其他": u"其他", u"外资存活": u"存续", u"证照管理登记中": u"在业", u"该企业已停业（个体工商户使用": u"停业", u"清算中": u"清算",
    u"注吊销": u"注销", u"迁移异地": u"迁出", u"被吊销未办理注销": u"吊销", u"吊销，已注销": u"注销", u"停业": u"停业", u"吊销并注销": u"注销",
    u"外资注销": u"注销", u"该企业已迁移异地": u"迁出", u"设立登记中": u"在业", u"待迁入": u"迁入", u"备案登记中": u"在业", u"资料修改": u"迁出",
    u"歇业": u"停业",
    u"已迁出企业": u"迁出", u"存续(经营正常)": u"存续", u"个体转企业": u"在业", u"市外迁出": u"迁出", u"清算": u"清算", u"该企业已撤销登记": u"撤销",
    u"系统内迁入中": u"迁入",
    u"正常在业": u"在业", u"吊销,未注销": u"吊销", u"注销登记中": u"注销", u"迁移": u"迁出", u"撤销": u"撤销", u"名称变更预先核准中": u"在业",
    u"年检中": u"在业", u"迁往外省市": u"迁出",
    u"筹建": u"筹建", u"迁出登记中": u"迁出", u"准迁": u"迁入", u"已转企": u"在业", u"被吊销办理注销": u"注销", u"吊销,已注销": u"注销",
    u"简易注销": u"注销", u"拟注销": u"注销",
    u"被吊销": u"吊销", u"迁入意见中": u"迁入", u"开业经营异常": u"开业", u"注销 （注销日期2001年5月30日）": u"注销", u"条线变更": u"开业",
    u"名称预核": u"开业", u"已撤销登记": u"撤销", u"已迁出": u"迁出",
    u"注销 （注销日期2001年5月25日）": u"注销", u"删除统一码业务中": u"注销", u"撤销登记": u"撤销", u"注销 （注销日期2002年9月26日）": u"注销",
    u"注销 （注销日期2013年4月3日）": u"注销", u"注销 （注销日期2015年7月23日）": u"注销",
    u"迁往市外": u"迁出", u"企业改制更新中": u"在业", u"已撤销企业": u"撤销", u"撤消登记": u"撤消", u"撤销企业": u"撤消", u"条线变出": u"开业",
    u"注销 （注销日期2002年8月26日）": u"注销", u"注销 （注销日期2002年9月18日）": u"注销",
    u"注销 （注销日期2013年6月14日）": u"注销", u"注销 （注销日期2013年8月6日）": u"注销", u"注销 （注销日期2015年8月31日）": u"注销",
    u"注销 （注销日期2016年2月26日）": u"注销", u"被撤销": u"撤销", u"吊销已注销": u"注销"
}

used_name_change_item_list = [
    #u"母公司名称",
    u"集团名称",
    u"名称简称",
    #u"隶属企业/集团母公司变更",
    u"名称变更",
    u"集团名称变更",
    #u"母公司名称变更",
    u"企业集团简称",
    u"企业名称",
    u"公司名称",
    u"企业名称（外文）",
    #u"母公司变更",
    #u"隶属企业名称（中文）",
    u"企业（机构）名称",
    u"机构名称",
    #u"分公司变更备案",
    #u"主机构名称",
    u"名称变更（字号名称、集团名称等",
    #u"分公司增加备案",
    u"集团简称",
    #u"隶属单位名称",
    #u"隶属企业名",
    #u"隶属企业中文名称",
    u"名称变更",
    u"名称变更（字号名称、集团名称等）变更",
    u"名称变更（字号名称、集团名称等",
    u"企业名称变更",
    u"企业名称",
    u"名称",
    u"企业(机构)名称",
    u"企业名称（外文）",
    u"改制变更",
]

fobidden_str_list = [
    u':',
    u'***',
    u'、',
    u'【',
    u'】',
    u'邮政编码',
    u'注册号',
    u'注册资金',
    u'企业名称',
    u'经营范围',
    u'行业代码',
    u'企业类型',
    u'一般经营项目',
    u'股东名称',

    u'增加备案',
    u'章程备案',

    u'增加字号',
    u'变更字号',
    u'字号名称',

    u'变更企业名称',
    u'名称变更',

    u'变更前',
    u'变更后',

    u'变更为',
]

prefix_cut_list = [
    u'名称变更',
]
gsxx_key_list = [
    "company",
    "province",
    "registered_capital",
    "business_scope",
    "legal_man",
    "trademark",
    "period",
    "registered_date",
    "registered_code",
    "address",
    "enterprise_type",
    "key_person",
    "registered_address",
    "business_status",
    "shareholder_information",
    "changerecords",
    "hezhun_date",
    "branch",
    "invested_companies",
    "investor_change",
    "src_registered_capital",
    "unified_social_credit_code",
    "industry",
    "registered_capital_unit",
    "stock_code",
    "contributor_information",
]