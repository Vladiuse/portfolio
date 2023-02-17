{% load code %}

{%lang 'sql' %}
-- some coment
SELECT id,app,name FROM django_migrations
WHERE id NOT IN (1,2,3)
GROUP BY app ORDER BY name DESC;
{%end%}
<pre>
 id |     app      |                   name
----+--------------+------------------------------------------
  1 | contenttypes | 0001_initial
  2 | auth         | 0001_initial
  3 | admin        | 0001_initial
  4 | admin        | 0002_logentry_remove_auto_add
  5 | admin        | 0003_logentry_add_action_flag_choices
  6 | contenttypes | 0002_remove_content_type_name
  7 | auth         | 0002_alter_permission_name_max_length
  8 | auth         | 0003_alter_user_email_max_length
  9 | auth         | 0004_alter_user_username_opts
 10 | auth         | 0005_alter_user_last_login_null
 11 | auth         | 0006_require_contenttypes_0002
 12 | auth         | 0007_alter_validators_add_error_messages
 13 | auth         | 0008_alter_user_username_max_length
 14 | auth         | 0009_alter_user_last_name_max_length
 15 | auth         | 0010_alter_group_name_max_length
 16 | auth         | 0011_update_proxy_permissions
 17 | auth         | 0012_alter_user_first_name_max_length
 18 | sessions     | 0001_initial
 30 | xxx          | 0001_initial
 31 | xxx          | 0002_language_man_lang
 32 | xxx          | 0003_remove_man_lang_man_lang
</pre>

{%lang 'sql' %}
-- some coment
SELECT id,app,name FROM django_migrations
WHERE id NOT IN (1,2,3)
GROUP BY app ORDER BY name DESC;
{%end%}
<pre>
 id |     app      |                   name
----+--------------+------------------------------------------
  1 | contenttypes | 0001_initial
  2 | auth         | 0001_initial
  3 | admin        | 0001_initial
  4 | admin        | 0002_logentry_remove_auto_add
  5 | admin        | 0003_logentry_add_action_flag_choices
  6 | contenttypes | 0002_remove_content_type_name
  7 | auth         | 0002_alter_permission_name_max_length
  8 | auth         | 0003_alter_user_email_max_length
  9 | auth         | 0004_alter_user_username_opts
 10 | auth         | 0005_alter_user_last_login_null
 11 | auth         | 0006_require_contenttypes_0002
 12 | auth         | 0007_alter_validators_add_error_messages
 13 | auth         | 0008_alter_user_username_max_length
 14 | auth         | 0009_alter_user_last_name_max_length
 15 | auth         | 0010_alter_group_name_max_length
 16 | auth         | 0011_update_proxy_permissions
 17 | auth         | 0012_alter_user_first_name_max_length
 18 | sessions     | 0001_initial
 30 | xxx          | 0001_initial
 31 | xxx          | 0002_language_man_lang
 32 | xxx          | 0003_remove_man_lang_man_lang
</pre>
