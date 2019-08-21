import { InformationService } from './../../providers/information.service';
import { Component, OnDestroy, OnInit } from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { takeWhile } from 'rxjs/operators';
import { SolarData } from '../../@core/data/solar';

interface CardSettings {
  title: string;
  iconClass: string;
  type: string;
}

@Component({
  selector: 'ngx-dashboard',
  styleUrls: ['./dashboard.component.scss'],
  templateUrl: './dashboard.component.html'
})
export class DashboardComponent implements OnDestroy, OnInit {
  private alive = true;

  solarValue: number;
  lightCard: CardSettings = {
    title: 'Light',
    iconClass: 'nb-lightbulb',
    type: 'primary'
  };
  rollerShadesCard: CardSettings = {
    title: 'Roller Shades',
    iconClass: 'nb-roller-shades',
    type: 'success'
  };
  wirelessAudioCard: CardSettings = {
    title: 'Wireless Audio',
    iconClass: 'nb-audio',
    type: 'info'
  };
  coffeeMakerCard: CardSettings = {
    title: 'Coffee Maker',
    iconClass: 'nb-coffee-maker',
    type: 'warning'
  };

  statusCards: string;

  commonStatusCardsSet: CardSettings[] = [
    this.lightCard,
    this.rollerShadesCard,
    this.wirelessAudioCard,
    this.coffeeMakerCard
  ];

  statusCardsByThemes: {
    default: CardSettings[];
    cosmic: CardSettings[];
    corporate: CardSettings[];
    dark: CardSettings[];
  } = {
    default: this.commonStatusCardsSet,
    cosmic: this.commonStatusCardsSet,
    corporate: [
      {
        ...this.lightCard,
        type: 'warning'
      },
      {
        ...this.rollerShadesCard,
        type: 'primary'
      },
      {
        ...this.wirelessAudioCard,
        type: 'danger'
      },
      {
        ...this.coffeeMakerCard,
        type: 'info'
      }
    ],
    dark: this.commonStatusCardsSet
  };

  tips = [];
  loading = false;
  error = false;

  constructor(
    private themeService: NbThemeService,
    private solarService: SolarData,
    private infoService: InformationService
  ) {
    this.themeService
      .getJsTheme()
      .pipe(takeWhile(() => this.alive))
      .subscribe(theme => {
        this.statusCards = this.statusCardsByThemes[theme.name];
      });

    this.solarService
      .getSolarData()
      .pipe(takeWhile(() => this.alive))
      .subscribe(data => {
        this.solarValue = data;
      });
  }

  ngOnInit() {
    this.infoService
      .fetchTips()
      .then(data => {
        this.loading = true;
        if (data && data) {
          // console.log(data['results']);
          for (const x in data['results']) {
            if (data['results'] && data['results'][x]) {
              // console.log('list: ', data['results'][x]);
              if (data['results'][x] && data['results'][x].tip) {
                // console.log('tip:', data['results'][x].tip);
                this.tips.push({
                  tip: data['results'][x].tip
                });
              }
            }
          }
        }
        this.loading = false;
      })
      .catch(err => {
        console.log(err);
        this.error = true;
      });
  }

  ngOnDestroy() {
    this.alive = false;
  }
}
