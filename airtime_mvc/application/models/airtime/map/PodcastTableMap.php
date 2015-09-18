<?php



/**
 * This class defines the structure of the 'podcast' table.
 *
 *
 *
 * This map class is used by Propel to do runtime db structure discovery.
 * For example, the createSelectSql() method checks the type of a given column used in an
 * ORDER BY clause to know whether it needs to apply SQL to make the ORDER BY case-insensitive
 * (i.e. if it's a text column type).
 *
 * @package    propel.generator.airtime.map
 */
class PodcastTableMap extends TableMap
{

    /**
     * The (dot-path) name of this class
     */
    const CLASS_NAME = 'airtime.map.PodcastTableMap';

    /**
     * Initialize the table attributes, columns and validators
     * Relations are not initialized by this method since they are lazy loaded
     *
     * @return void
     * @throws PropelException
     */
    public function initialize()
    {
        // attributes
        $this->setName('podcast');
        $this->setPhpName('Podcast');
        $this->setClassname('Podcast');
        $this->setPackage('airtime');
        $this->setUseIdGenerator(true);
        $this->setPrimaryKeyMethodInfo('podcast_id_seq');
        // columns
        $this->addPrimaryKey('id', 'DbId', 'INTEGER', true, null, null);
        $this->addColumn('url', 'DbUrl', 'VARCHAR', true, 256, null);
        $this->addColumn('title', 'DbTitle', 'VARCHAR', true, 256, null);
        $this->addColumn('creator', 'DbCreator', 'VARCHAR', false, 256, null);
        $this->addColumn('description', 'DbDescription', 'VARCHAR', false, 512, null);
        $this->addColumn('auto_ingest', 'DbAutoIngest', 'BOOLEAN', true, null, false);
        $this->addForeignKey('owner', 'DbOwner', 'INTEGER', 'cc_subjs', 'id', false, null, null);
        $this->addColumn('type', 'DbType', 'INTEGER', true, null, 1);
        // validators
    } // initialize()

    /**
     * Build the RelationMap objects for this table relationships
     */
    public function buildRelations()
    {
        $this->addRelation('CcSubjs', 'CcSubjs', RelationMap::MANY_TO_ONE, array('owner' => 'id', ), 'CASCADE', null);
        $this->addRelation('PodcastEpisodes', 'PodcastEpisodes', RelationMap::ONE_TO_MANY, array('id' => 'podcast_id', ), 'CASCADE', null, 'PodcastEpisodess');
    } // buildRelations()

} // PodcastTableMap
