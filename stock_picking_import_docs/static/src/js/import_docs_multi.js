odoo.define('stock_picking_import_docs.FieldImportDocsMulti', function (require) {
    'use strict';

    var fieldRegistry = require('web.field_registry');
    var relationalFields = require('web.relational_fields');
    var FieldMany2ManyBinaryMultiFiles =
        relationalFields.FieldMany2ManyBinaryMultiFiles;

    var FieldImportDocsMulti = FieldMany2ManyBinaryMultiFiles.extend({
        /**
         * Serve files inline so the browser previews them in a new tab.
         *
         * @override
         */
        _getFileUrl: function (attachment) {
            return '/web/content/' + attachment.id;
        },

        /**
         * @override
         */
        _render: function () {
            this._super.apply(this, arguments);
            this.$('.o_attachment a[href]').attr('target', '_blank');
        },
    });

    fieldRegistry.add('import_docs_multi', FieldImportDocsMulti);

    return FieldImportDocsMulti;
});
