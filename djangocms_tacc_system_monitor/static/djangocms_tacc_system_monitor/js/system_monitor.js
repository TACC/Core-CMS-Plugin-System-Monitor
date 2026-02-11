/**
 * Show public runtime data about a TACC system
 *
 * - Manipulates attributes and text nodes within existing markup.
 * - Data is NOT dynamically updated after initial load.
 * @module systemMonitor
 */
// GH-295: Use server-side logic instead of client-side



/* Definitions */

/**
 * All system data
 * @typedef {array<module:systemMonitor~System>} AllSystems
 * @see https://frontera-portal.tacc.utexas.edu/api/system-monitor/
 */

/**
 * Single system data
 * @typedef {object} System
 * @see https://frontera-portal.tacc.utexas.edu/api/system-monitor/
 */



/* Constants */
/* IDEA: These could be static properties, once Safari support is widespread */

/**
 * Sample system data
 * @type {array<module:systemMonitor~System>}
 */
const API_SAMPLE_DATA = JSON.parse('[{"display_name": "Stampede3", "hostname": "stampede3.tacc.utexas.edu", "resource_type": "COMPUTE", "load_percentage": 86, "jobs": {"running": 486, "queued": 261}, "online": true, "reachable": true, "queues_down": false, "in_maintenance": false, "is_operational": true}, {"display_name": "Lonestar6", "hostname": "ls6.tacc.utexas.edu", "resource_type": "COMPUTE", "load_percentage": 99, "jobs": {"running": 356, "queued": 1238}, "online": true, "reachable": true, "queues_down": false, "in_maintenance": false, "is_operational": true}, {"display_name": "Frontera", "hostname": "frontera.tacc.utexas.edu", "resource_type": "COMPUTE", "load_percentage": 92, "jobs": {"running": 400, "queued": 35}, "online": true, "reachable": true, "queues_down": false, "in_maintenance": false, "is_operational": true}, {"display_name": "Vista", "hostname": "vista.tacc.utexas.edu", "resource_type": "COMPUTE", "load_percentage": 100, "jobs": {"running": 208, "queued": 41}, "online": true, "reachable": true, "queues_down": false, "in_maintenance": false, "is_operational": true}]');
/**
 * The URL of the API endpoint
 * @type {string}
 */
const API_URL = '/api/system-monitor';



/* Exports */

/**
 * Populate a system monitor element
 */
export class SystemMonitor {



  /**
   * Initialize system monitor
   * @param {string} hostname - The systems to show
   * @param {HTMLElement} domElement - The DOM element for display
   * @param {HTMLElement} [shouldUseSampleData=false] - Whether to present fake data
   */
  constructor(hostname, domElement, shouldUseSampleData=false) {
    /**
     * The systems to show
     * @type {string}
     */
    this.hostname = hostname;

    /**
     * The DOM element for display
     * @type {HTMLElement}
     */
    this.domElement = domElement;

    /**
     * Whether to present fake data on a local server
     * @type {boolean}
     */
    this.shouldUseSampleData = shouldUseSampleData;



    this.init();
  }



  /**
   * Load system status
   * @param {string} path
   * @param {function} onSuccess - Callback for success (receives JSON)
   * @param {function} onError - Callback for success (receives XMLHttpRequest)
   */
  loadStatus(path, onSuccess, onError) {
    const xhr = new XMLHttpRequest();

    xhr.onreadystatechange = () => {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          if (onSuccess) onSuccess(JSON.parse(xhr.responseText));
        } else {
          if (onError) onError(xhr);
        }
      }
    };
    xhr.open('GET', path, true);
    xhr.send();
  }

  /**
   * Whether system is operational
   * @param {module:systemMonitor~System} system
   * @return {boolean}
   */
  isOperational(system) {
    return (system['is_operational'] === true);
  }

  /**
   * Get element in UI by an ID
   * @param {string} id - The (internally unique) identifier of an element
   * @return {HTMLElement}
   */
  getElement(id) {
    // To permit multiple instances, we must NOT use `id` attribute
    return this.domElement.querySelector(`[data-id="${id}"]`);
  }

  /**
   * Show system content in UI
   */
  showStatus() {
    this.getElement('status').classList.remove('d-none');
  }

  /**
   * Style system status
   * @param {string} type - A type: "warning"
   */
  populateStatus(type) {
    const element = this.getElement('status');

    switch (type) {
      case 'warning':
        element.classList.remove('badge-success');
        element.removeAttribute('data-icon');
        element.innerHTML = 'Maintenance';
        element.classList.add('badge-warning');

      default:
        break;
    }
  }

  /**
   * Populate system load
   * @param {module:systemMonitor~System} system
   */
  populateLoad(system) {
    this.getElement('load_percentage').innerHTML =
      system['load_percentage'] + '%';
    this.getElement('jobs_running').innerHTML =
      system['jobs']['running'];
    this.getElement('jobs_queued').innerHTML =
      system['jobs']['queued'];
  }

  /**
   * Populate monitor based on data
   * @param {module:systemMonitor~AllSystems} availableSystems
   */
  populate(availableSystems) {
    const system = availableSystems.find(
      (availableSystem) => availableSystem['hostname'] === this.hostname
    );
    const isOperational = this.isOperational(system);

    if (system) {
      console.info(`System Monitor: System found (${this.hostname})`);
    } else {
      console.error(`System Monitor: System not found (${this.hostname})`);
    }

    if (system && isOperational) {
      this.populateLoad(system);
    } else {
      this.populateStatus('warning');
      if (system) {
        this.populateLoad(system);
      }
    }
    this.showStatus();
  }

  /* Initialize (if using a class, Constructor) */

  /** Load and populate UI */
  init() {
    document.addEventListener(
      'DOMContentLoaded',
      () => {
        this.loadStatus(
          API_URL,
          (data) => {
            this.populate(data);
          },
          (xhr) => {
            if (this.shouldUseSampleData) {
              this.populate(API_SAMPLE_DATA);
            } else {
              console.error(xhr);
            }
          }
        );

        console.log('System Monitor: Load complete');
      },
      false
    );
  }
}
