# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
patch_list = [
	"execute:webnotes.reload_doc('core', 'doctype', 'doctype', force=True) #2013-07-15",
	"execute:webnotes.reload_doc('core', 'doctype', 'docfield', force=True) #2013-07-15",
	"execute:webnotes.reload_doc('core', 'doctype', 'doctype', force=True) #2013-07-16",
	"execute:webnotes.reload_doc('core', 'doctype', 'docfield', force=True) #2013-07-16",
	"execute:webnotes.reload_doc('core', 'doctype', 'docperm') #2013-07-16",
	"execute:webnotes.reload_doc('core', 'doctype', 'page') #2013-07-16",
	"execute:webnotes.reload_doc('core', 'doctype', 'report') #2013-07-16",
	"patches.mar_2012.clean_property_setter", 
	"patches.april_2012.naming_series_patch", 
	"patches.mar_2012.cleanup_control_panel", 
	"patches.mar_2012.doctype_get_refactor", 
	"patches.mar_2012.delete_docformat", 
	"patches.mar_2012.usertags", 
	"patches.april_2012.reload_c_form", 
	"patches.april_2012.after_sync_cleanup", 
	"patches.april_2012.remove_default_from_rv_detail", 
	"patches.april_2012.update_role_in_address", 
	"patches.april_2012.update_permlevel_in_address", 
	"patches.april_2012.update_appraisal_permission", 
	"patches.april_2012.repost_stock_for_posting_time", 
	"patches.may_2012.cleanup_property_setter", 
	"patches.may_2012.rename_prev_doctype", 
	"patches.may_2012.cleanup_notification_control", 
	"patches.may_2012.stock_reco_patch", 
	"patches.may_2012.page_role_series_fix", 
	"patches.may_2012.reload_sales_invoice_pf", 
	"patches.may_2012.std_pf_readonly", 
	"patches.may_2012.customize_form_cleanup", 
	"patches.may_2012.cs_server_readonly", 
	"patches.may_2012.clear_session_cache", 
	"patches.may_2012.same_purchase_rate_patch", 
	"patches.may_2012.create_report_manager_role", 
	"patches.may_2012.profile_perm_patch", 
	"patches.may_2012.remove_euro_currency", 
	"patches.may_2012.remove_communication_log", 
	"patches.june_2012.barcode_in_feature_setup", 
	"patches.june_2012.copy_uom_for_pur_inv_item", 
	"patches.june_2012.fetch_organization_from_lead", 
	"patches.june_2012.reports_list_permission", 
	"patches.june_2012.support_ticket_autoreply", 
	"patches.june_2012.series_unique_patch", 
	"patches.june_2012.set_recurring_type", 
	"patches.june_2012.alter_tabsessions", 
	"patches.june_2012.delete_old_parent_entries", 
	"patches.april_2012.delete_about_contact", 
	"patches.july_2012.reload_pr_po_mapper", 
	"patches.july_2012.address_contact_perms", 
	"patches.july_2012.packing_list_cleanup_and_serial_no", 
	"patches.july_2012.deprecate_import_data_control", 
	"patches.july_2012.default_freeze_account", 
	"patches.july_2012.update_purchase_tax", 
	"patches.june_2012.cms2", 
	"patches.july_2012.auth_table", 
	"patches.july_2012.remove_event_role_owner_match", 
	"patches.july_2012.deprecate_bulk_rename", 
	"patches.july_2012.bin_permission", 
	"patches.july_2012.project_patch_repeat", 
	"patches.july_2012.repost_stock_due_to_wrong_packing_list", 
	"patches.august_2012.task_allocated_to_assigned", 
	"patches.august_2012.change_profile_permission", 
	"patches.august_2012.repost_billed_amt", 
	"patches.september_2012.stock_report_permissions_for_accounts", 
	"patches.september_2012.communication_delete_permission", 
	"patches.september_2012.all_permissions_patch", 
	"patches.september_2012.customer_permission_patch", 
	"patches.september_2012.add_stock_ledger_entry_index", 
	"patches.september_2012.plot_patch", 
	"patches.september_2012.event_permission", 
	"patches.september_2012.repost_stock", 
	"patches.september_2012.rebuild_trees", 
	"patches.september_2012.deprecate_account_balance", 
	"patches.september_2012.profile_delete_permission", 
	"patches.october_2012.update_permission", 
	"patches.october_2012.fix_wrong_vouchers", 
	"patches.october_2012.company_fiscal_year_docstatus_patch", 
	"patches.october_2012.update_account_property", 
	"patches.october_2012.fix_cancelled_gl_entries", 
	"patches.october_2012.custom_script_delete_permission", 
	"patches.november_2012.custom_field_insert_after", 
	"patches.november_2012.report_permissions", 
	"patches.november_2012.customer_issue_allocated_to_assigned", 
	"patches.november_2012.reset_appraisal_permissions", 
	"patches.november_2012.disable_cancelled_profiles", 
	"patches.november_2012.support_ticket_response_to_communication", 
	"patches.november_2012.cancelled_bom_patch", 
	"patches.november_2012.communication_sender_and_recipient", 
	"patches.november_2012.update_delivered_billed_percentage_for_pos", 
	"patches.november_2012.add_theme_to_profile", 
	"patches.november_2012.add_employee_field_in_employee", 
	"patches.november_2012.leave_application_cleanup", 
	"patches.november_2012.production_order_patch", 
	"patches.november_2012.gle_floating_point_issue", 
	"patches.december_2012.deprecate_tds", 
	"patches.december_2012.expense_leave_reload", 
	"patches.december_2012.repost_ordered_qty", 
	"patches.december_2012.repost_projected_qty", 
	"patches.december_2012.website_cache_refactor", 
	"patches.december_2012.production_cleanup", 
	"patches.december_2012.fix_default_print_format", 
	"patches.december_2012.file_list_rename", 
	"patches.december_2012.replace_createlocal", 
	"patches.december_2012.remove_quotation_next_contact", 
	"patches.december_2012.stock_entry_cleanup", 
	"patches.december_2012.production_order_naming_series", 
	"patches.december_2012.rebuild_item_group_tree", 
	"patches.december_2012.address_title", 
	"patches.december_2012.delete_form16_print_format", 
	"patches.december_2012.update_print_width", 
	"patches.january_2013.remove_bad_permissions", 
	"patches.january_2013.holiday_list_patch", 
	"patches.january_2013.stock_reconciliation_patch", 
	"patches.january_2013.report_permission", 
	"patches.january_2013.give_report_permission_on_read", 
	"patches.january_2013.update_closed_on",
	"patches.january_2013.change_patch_structure",
	"patches.january_2013.update_country_info",
	"patches.january_2013.remove_tds_entry_from_gl_mapper",
	"patches.january_2013.update_number_format",
	"patches.january_2013.purchase_price_list",
	"execute:webnotes.reload_doc('core', 'doctype', 'print_format') #2013-01",
	"execute:webnotes.reload_doc('accounts','Print Format','Payment Receipt Voucher')",
	"patches.january_2013.update_fraction_for_usd",
	"patches.january_2013.enable_currencies",
	"patches.january_2013.remove_unwanted_permission",
	"patches.january_2013.remove_landed_cost_master",
	"patches.january_2013.reload_print_format",
	"patches.january_2013.rebuild_tree",
	"execute:webnotes.reload_doc('core','doctype','docfield') #2013-01-28",
	"patches.january_2013.tabsessions_to_myisam",
	"patches.february_2013.remove_gl_mapper",
	"patches.february_2013.reload_bom_replace_tool_permission",
	"patches.february_2013.payment_reconciliation_reset_values",
	"patches.february_2013.account_negative_balance",
	"patches.february_2013.remove_account_utils_folder",
	"patches.february_2013.update_company_in_leave_application",
	"execute:webnotes.conn.sql_ddl('alter table tabSeries change `name` `name` varchar(100)')",
	"execute:webnotes.conn.sql('update tabUserRole set parentfield=\"user_roles\" where parentfield=\"userroles\"')",
	"patches.february_2013.p01_event",
	"execute:webnotes.delete_doc('Page', 'Calendar')",
	"patches.february_2013.p02_email_digest",
	"patches.february_2013.p03_material_request",
	"patches.february_2013.p04_remove_old_doctypes",
	"execute:webnotes.delete_doc('DocType', 'Plot Control')",
	"patches.february_2013.p05_leave_application",
	"patches.february_2013.gle_floating_point_issue_revisited",
	"patches.february_2013.fix_outstanding",
	"execute:webnotes.delete_doc('DocType', 'Service Order')",
	"execute:webnotes.delete_doc('DocType', 'Service Quotation')",
	"execute:webnotes.delete_doc('DocType', 'Service Order Detail')",
	"execute:webnotes.delete_doc('DocType', 'Service Quotation Detail')",
	"execute:webnotes.delete_doc('Page', 'Query Report')",
	"patches.february_2013.repost_reserved_qty",
	"execute:webnotes.reload_doc('core', 'doctype', 'report') # 2013-02-25",
	"execute:webnotes.conn.sql(\"update `tabReport` set report_type=if(ifnull(query, '')='', 'Report Builder', 'Query Report') where is_standard='No'\")",
	"execute:webnotes.conn.sql(\"update `tabReport` set report_name=name where ifnull(report_name,'')='' and is_standard='No'\")",
	"patches.february_2013.p08_todo_query_report",
	"execute:(not webnotes.conn.exists('Role', 'Projects Manager')) and webnotes.doc({'doctype':'Role', 'role_name':'Projects Manager'}).insert()",
	"patches.february_2013.p09_remove_cancelled_warehouses",
	"patches.march_2013.update_po_prevdoc_doctype",
	"patches.february_2013.p09_timesheets",
	"execute:(not webnotes.conn.exists('UOM', 'Hour')) and webnotes.doc({'uom_name': 'Hour', 'doctype': 'UOM', 'name': 'Hour'}).insert()",
	"patches.march_2013.p01_c_form",
	"execute:webnotes.conn.sql('update tabDocPerm set `submit`=1, `cancel`=1, `amend`=1 where parent=\"Time Log\"')",
	"execute:webnotes.delete_doc('DocType', 'Attendance Control Panel')",
	"patches.march_2013.p02_get_global_default",
	"patches.march_2013.p03_rename_blog_to_blog_post",
	"patches.march_2013.p04_pos_update_stock_check",
	"patches.march_2013.p05_payment_reconciliation",
	"patches.march_2013.p06_remove_sales_purchase_return_tool",
	"execute:webnotes.bean('Global Defaults').save()",
	"patches.march_2013.p07_update_project_in_stock_ledger",
	"execute:webnotes.reload_doc('stock', 'doctype', 'item') #2013-03-25",
	"execute:webnotes.reload_doc('setup', 'doctype', 'item_group') #2013-03-25",
	"execute:webnotes.reload_doc('website', 'doctype', 'blog_post') #2013-03-25",
	"execute:webnotes.reload_doc('website', 'doctype', 'web_page') #2013-03-25",
	"execute:webnotes.reload_doc('setup', 'doctype', 'sales_partner') #2013-06-25",
	"execute:webnotes.conn.set_value('Email Settings', None, 'send_print_in_body_and_attachment', 1)",
	"patches.march_2013.p10_set_fiscal_year_for_stock",
	"patches.march_2013.p10_update_against_expense_account",
	"patches.march_2013.p11_update_attach_files",
	"patches.march_2013.p12_set_item_tax_rate_in_json",
	"patches.march_2013.p07_update_valuation_rate",
	"patches.march_2013.p08_create_aii_accounts",
	"patches.april_2013.p01_update_serial_no_valuation_rate",
	"patches.april_2013.p02_add_country_and_currency",
	"patches.april_2013.p03_fixes_for_lead_in_quotation",
	"patches.april_2013.p04_reverse_modules_list",
	"patches.april_2013.p04_update_role_in_pages",
	"patches.april_2013.p05_update_file_data",
	"patches.april_2013.p06_update_file_size",
	"patches.april_2013.p05_fixes_in_reverse_modules",
	"patches.april_2013.p07_rename_cost_center_other_charges",
	"patches.april_2013.p06_default_cost_center",
	"execute:webnotes.reset_perms('File Data')",
	"patches.april_2013.p07_update_file_data_2",
	"patches.april_2013.rebuild_sales_browser",
	"patches.may_2013.p01_selling_net_total_export",
	"patches.may_2013.repost_stock_for_no_posting_time",
	"patches.may_2013.p01_conversion_factor_and_aii",
	"patches.may_2013.p02_update_valuation_rate",
	"patches.may_2013.p03_update_support_ticket",
	"patches.may_2013.p04_reorder_level",
	"patches.may_2013.p05_update_cancelled_gl_entries",
	"patches.may_2013.p06_make_notes",
	"patches.may_2013.p06_update_billed_amt_po_pr",
	"patches.may_2013.p07_move_update_stock_to_pos",
	"patches.may_2013.p08_change_item_wise_tax",
	"patches.june_2013.p01_update_bom_exploded_items",
	"patches.june_2013.p02_update_project_completed",
	"execute:webnotes.delete_doc('DocType', 'System Console')",
	"patches.june_2013.p03_buying_selling_for_price_list",
	"patches.june_2013.p04_fix_event_for_lead_oppty_project",
	"patches.june_2013.p05_remove_search_criteria_reports",
	"execute:webnotes.delete_doc('Report', 'Sales Orders Pending To Be Delivered')",
	"patches.june_2013.p05_remove_unused_doctypes",
	"patches.june_2013.p06_drop_unused_tables",
	"patches.june_2013.p07_taxes_price_list_for_territory",
	"patches.june_2013.p08_shopping_cart_settings",
	"patches.june_2013.p09_update_global_defaults",
	"patches.june_2013.p10_lead_address",
	"patches.july_2013.p01_remove_doctype_mappers",
	"execute:webnotes.delete_doc('Report', 'Delivered Items To Be Billed')",
	"execute:webnotes.delete_doc('Report', 'Received Items To Be Billed')",
	"patches.july_2013.p02_copy_shipping_address",
	"patches.july_2013.p03_cost_center_company",
	"execute:webnotes.bean('Style Settings').save() #2013-07-16",
	"patches.july_2013.p04_merge_duplicate_leads",
	"patches.july_2013.p05_custom_doctypes_in_list_view",
	"patches.july_2013.p06_same_sales_rate",
	"patches.july_2013.p07_repost_billed_amt_in_sales_cycle",
	"execute:webnotes.reload_doc('accounts', 'Print Format', 'Sales Invoice Classic') # 2013-07-22",
	"execute:webnotes.reload_doc('accounts', 'Print Format', 'Sales Invoice Modern') # 2013-07-22",
	"execute:webnotes.reload_doc('accounts', 'Print Format', 'Sales Invoice Spartan') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Quotation Classic') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Quotation Modern') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Quotation Spartan') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Sales Order Classic') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Sales Order Modern') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Sales Order Spartan') # 2013-07-22",
	"execute:webnotes.reload_doc('stock', 'Print Format', 'Delivery Note Classic') # 2013-07-22",
	"execute:webnotes.reload_doc('stock', 'Print Format', 'Delivery Note Modern') # 2013-07-22",
	"execute:webnotes.reload_doc('stock', 'Print Format', 'Delivery Note Spartan') # 2013-07-22",
	"patches.july_2013.p08_custom_print_format_net_total_export",
	"patches.july_2013.p09_remove_website_pyc",
	"patches.july_2013.p10_change_partner_user_to_website_user",
	"patches.july_2013.p11_update_price_list_currency",
	"execute:webnotes.bean('Selling Settings').save() #2013-07-29",
	"patches.august_2013.p01_hr_settings",
	"patches.august_2013.p02_rename_price_list",
	"patches.august_2013.p03_pos_setting_replace_customer_account",
	"patches.august_2013.p05_update_serial_no_status",
	"patches.august_2013.p05_employee_birthdays",
	"execute:webnotes.reload_doc('accounts', 'Print Format', 'POS Invoice') # 2013-08-16",
	# "patches.august_2013.p06_fix_sle_against_stock_entry",
]