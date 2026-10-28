odoo.define('stock_picking_import_docs.FieldImportDocsMulti', function (require) {
    'use strict';

    var fieldRegistry = require('web.field_registry');
    var relationalFields = require('web.relational_fields');
    var FieldMany2ManyBinaryMultiFiles =
        relationalFields.FieldMany2ManyBinaryMultiFiles;

    /**
     * Multi file upload widget rendering attachment icon blocks.
     * Clicking a file opens it inline in a new tab (browser preview)
     * instead of downloading it.
     */
    var FieldImportDocsMulti = FieldMany2ManyBinaryMultiFiles.extend({
        /**
         * Serve files inline so the browser previews them.
         *
         * @override
         */
        _getFileUrl: function (attachment) {
            return '/web/content/' + attachment.id;
        },

        /**
         * Open previews in a new tab so the form isn't left.
         *
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
